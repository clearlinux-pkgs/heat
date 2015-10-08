#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : heat
Version  : 5.0.0.0rc2
Release  : 9
URL      : http://tarballs.openstack.org/heat/heat-5.0.0.0rc2.tar.gz
Source0  : http://tarballs.openstack.org/heat/heat-5.0.0.0rc2.tar.gz
Source1  : heat-api-cfn.service
Source2  : heat-api.service
Source3  : heat-engine.service
Source4  : heat.tmpfiles
Summary  : OpenStack Orchestration
Group    : Development/Tools
License  : Apache-2.0
Requires: heat-bin
Requires: heat-python
Requires: heat-config
Requires: heat-data
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : Mako-python
BuildRequires : MarkupSafe-python
BuildRequires : MySQL-python-python
BuildRequires : PasteDeploy-python
BuildRequires : PyYAML-python
BuildRequires : Pygments
BuildRequires : Routes-python
BuildRequires : SQLAlchemy-python
BuildRequires : Sphinx-python
BuildRequires : Tempita-python
BuildRequires : WebOb-python
BuildRequires : aioeventlet-python
BuildRequires : alembic-python
BuildRequires : amqp-python
BuildRequires : anyjson-python
BuildRequires : cffi
BuildRequires : cffi-python
BuildRequires : cliff-python
BuildRequires : cmd2-python
BuildRequires : coverage-python
BuildRequires : croniter-python
BuildRequires : cryptography
BuildRequires : decorator-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : dogpile.core
BuildRequires : ecdsa-python
BuildRequires : enum34-python
BuildRequires : eventlet-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : funcsigs-python
BuildRequires : futures-python
BuildRequires : greenlet-python
BuildRequires : hacking
BuildRequires : httplib2
BuildRequires : idna-python
BuildRequires : ipaddress-python
BuildRequires : iso8601-python
BuildRequires : jsonpatch-python
BuildRequires : jsonpointer-python
BuildRequires : jsonschema-python
BuildRequires : keystonemiddleware
BuildRequires : kombu-python
BuildRequires : linecache2-python
BuildRequires : lxml-python
BuildRequires : mccabe-python
BuildRequires : mox-python
BuildRequires : mox3-python
BuildRequires : msgpack-python-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : oslo.cache
BuildRequires : oslo.concurrency-python
BuildRequires : oslo.config
BuildRequires : oslo.context-python
BuildRequires : oslo.db-python
BuildRequires : oslo.i18n-python
BuildRequires : oslo.log-python
BuildRequires : oslo.messaging-python
BuildRequires : oslo.middleware-python
BuildRequires : oslo.policy
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils-python
BuildRequires : oslo.versionedobjects-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : osprofiler-python
BuildRequires : paramiko-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : posix_ipc
BuildRequires : prettytable
BuildRequires : psycopg2-python
BuildRequires : py-python
BuildRequires : pyOpenSSL-python
BuildRequires : pyasn1-python
BuildRequires : pycadf-python
BuildRequires : pycparser
BuildRequires : pycparser-python
BuildRequires : pycrypto-python
BuildRequires : pyflakes-python
BuildRequires : pyparsing-python
BuildRequires : pytest
BuildRequires : python-ceilometerclient-python
BuildRequires : python-cinderclient-python
BuildRequires : python-dateutil
BuildRequires : python-designateclient
BuildRequires : python-dev
BuildRequires : python-glanceclient-python
BuildRequires : python-heatclient-python
BuildRequires : python-keystoneclient-python
BuildRequires : python-manilaclient
BuildRequires : python-mimeparse-python
BuildRequires : python-mistralclient
BuildRequires : python-mock
BuildRequires : python-neutronclient-python
BuildRequires : python-novaclient-python
BuildRequires : python-saharaclient-python
BuildRequires : python-swiftclient-python
BuildRequires : python-troveclient-python
BuildRequires : python-zaqarclient
BuildRequires : pytz-python
BuildRequires : qpid-python-python
BuildRequires : repoze.lru-python
BuildRequires : requests-python
BuildRequires : retrying-python
BuildRequires : setuptools
BuildRequires : simplejson
BuildRequires : six
BuildRequires : six-python
BuildRequires : sqlalchemy-migrate-python
BuildRequires : sqlparse
BuildRequires : stevedore
BuildRequires : testrepository-python
BuildRequires : testresources
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : trollius-python
BuildRequires : unittest2-python
BuildRequires : virtualenv
BuildRequires : warlock-python
Patch1: 0001-default-config.patch

%description
oslo-incubator
--------------
A number of modules from oslo-incubator are imported into this project.
You can clone the oslo-incubator repository using the following url:

%package bin
Summary: bin components for the heat package.
Group: Binaries
Requires: heat-data
Requires: heat-config

%description bin
bin components for the heat package.


%package config
Summary: config components for the heat package.
Group: Default

%description config
config components for the heat package.


%package data
Summary: data components for the heat package.
Group: Data

%description data
data components for the heat package.


%package python
Summary: python components for the heat package.
Group: Default
Requires: Babel-python
Requires: PasteDeploy-python
Requires: PyYAML-python
Requires: Routes-python
Requires: SQLAlchemy-python
Requires: WebOb-python
Requires: croniter-python
Requires: cryptography
Requires: eventlet-python
Requires: greenlet-python
Requires: keystonemiddleware
Requires: kombu-python
Requires: lxml-python
Requires: netaddr
Requires: oslo.concurrency-python
Requires: oslo.config
Requires: oslo.context-python
Requires: oslo.db-python
Requires: oslo.i18n-python
Requires: oslo.log-python
Requires: oslo.messaging-python
Requires: oslo.middleware-python
Requires: oslo.serialization-python
Requires: oslo.utils-python
Requires: oslo.versionedobjects-python
Requires: osprofiler-python
Requires: paramiko-python
Requires: pycrypto-python
Requires: python-ceilometerclient-python
Requires: python-cinderclient-python
Requires: python-glanceclient-python
Requires: python-heatclient-python
Requires: python-keystoneclient-python
Requires: python-neutronclient-python
Requires: python-novaclient-python
Requires: python-saharaclient-python
Requires: python-swiftclient-python
Requires: python-troveclient-python
Requires: pytz-python
Requires: requests-python
Requires: six-python
Requires: sqlalchemy-migrate-python
Requires: stevedore
Requires: testrepository-python
Requires: testscenarios
Requires: testtools-python

%description python
python components for the heat package.


%prep
%setup -q -n heat-5.0.0.0rc2
%patch1 -p1

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/heat-api-cfn.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/heat-api.service
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/heat-engine.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE4} %{buildroot}/usr/lib/tmpfiles.d/heat.conf
## make_install_append content
install -d -m 755 %{buildroot}/usr/share/defaults/heat
install -p -D -m 644 etc/heat/*.ini %{buildroot}/usr/share/defaults/heat/
install -p -D -m 644 etc/heat/*.json %{buildroot}/usr/share/defaults/heat/
install -p -D -m 644 etc/heat/heat.conf.sample %{buildroot}/usr/share/defaults/heat/heat.conf
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/heat-api
/usr/bin/heat-api-cfn
/usr/bin/heat-api-cloudwatch
/usr/bin/heat-db-setup
/usr/bin/heat-engine
/usr/bin/heat-keystone-setup
/usr/bin/heat-keystone-setup-domain
/usr/bin/heat-manage

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/heat-api-cfn.service
/usr/lib/systemd/system/heat-api.service
/usr/lib/systemd/system/heat-engine.service
/usr/lib/tmpfiles.d/heat.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/heat/api-paste.ini
/usr/share/defaults/heat/heat.conf
/usr/share/defaults/heat/policy.json

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
