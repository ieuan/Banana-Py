from setuptools import setup, find_packages

setup(
    name='banana_py',
    version='0.1.4',
    description='OAuth2 Backend for MailChimp',
    long_description='',
    keywords='django, mailchimp, oauth2',
    author='Ieuan Lovett <ieuan.lovett@gmail.com>',
    author_email='ieuan.lovett@gmail.com',
    url='https://github.com/ieuan/Banana-Py/',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['oauth2', 'simplejson', 'django'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
)
