========
BananaPy
========

BananaPy provides you with a way to authenticate your Django application with MailChimp's new OAuth2 service.

Installation and Usage
======================

BananaPy requires ``Python-OAuth2`` from SimpleGeo and the ``simplejson`` library, both of which should be installed
automatically if not already installed. You can get BananaPy from its Github repo (https://github.com/ieuan/Banana-Py/)

    pip install git+git://github.com/ieuan/Banana-Py.git#egg=banana-py

Let everything install and then set up your MailChimp app. Set the ``redirect uri`` on your MailChimp app to::

    http://your-domain.com/bananas/ripe/


Add ``banana_py`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'banana_py',
        ...
    )

Then add the following four settings to your ``settings.py``::

    MAILCHIMP_CLIENT_ID = '123456789'
    MAILCHIMP_CLIENT_SECRET = 'a1b2c3d4e5f6789'
    MAILCHIMP_REDIRECT_URI = 'http://your-domain.com/bananas/ripe/'
    MAILCHIMP_COMPLETE_URI = 'http://your-domain.com/'

The last setting, ``MAILCHIMP_COMPLETE_URI`` can be anything you want, a Profile page or some view of your own that creates
a user account for the new user.

Optional settings you can add::

    MAILCHIMP_COMPLETE_CALLBACK_MODULE = 'myapp.views'
    MAILCHIMP_COMPLETE_CALLBACK_FUNCTION = 'mcCallback'

Both of these settings must be used together, and allow you to choose a callback function which will be called once the calls to MailChimp have been completed

Add URLs entries::

    urlpatterns = patterns('',
        ...
        url(r'', include('banana_py.urls')),
        ...
    )

In the template(s) where you want to display the authorize link::

    {% load banana_tags %}
    {% banana_auth_link "Authorize" %}

This will print out an HTML anchor tag with the appropriate link and the supplied text as the link text.

Or to get just the url::

    {% load banana_tags %}
    <a href="{% banana_auth_url %}"><button>Connect to MailChimp</button></a>

Once the user completes the authorization workflow (and ends up on your ``MAILCHIMP_COMPLETE_URI`` view), their
MailChimp-provided authorization information will be available in the ``request.session`` object as ``mailchimp_details``.

Alternatively you can supply additional state information to allow your callback method to redirect to a different url on completion.

In your view::

    modelObject = get_object_or_404(MyModelObject, pk=kwargs['pk'])
    authState = {
        'modelObject': modelObject.id
    }

    context = {
        'modelObject': modelObject,
        'authState': urllib.parse.quote_plus(json.dumps(authState))
    }

    return render(request, 'myapp/detail.html', context)

In your template::

    <a href="{% banana_auth_url %}&state={{ authState }}">
        <button>Connect To MailChimp</button>
    </a>

Your callback view::

    def mcCallback(data):
        access_token = data['access_token']
        state = json.loads(data['request']['state'])

        modelObjectId = state['modelObject'] // From authState Dict

        modelObject = MyModelObject.objects.get(pk=modelObjectId)

        modelObject.access_token = access_token
        modelObject.save()

        data['redirect'] = modelObject.get_absolute_url()

        data['messages'] = {
            'success': 'Mailchimp Authentication Successful'
        }

        return data

Thanks
======

Our thanks to the MailChimp team for letting us build this bridge. Also to Joe Stump and the rest of the SimpleGeo team for making their awesome OAuth2 library. Also, thanks to the Django team, without whom this wouldn't really be needed!
