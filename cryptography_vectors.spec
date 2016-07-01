#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cryptography_vectors
Version  : 1.4
Release  : 28
URL      : http://pypi.debian.net/cryptography_vectors/cryptography_vectors-1.4.tar.gz
Source0  : http://pypi.debian.net/cryptography_vectors/cryptography_vectors-1.4.tar.gz
Summary  : Test vectors for the cryptography package.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: cryptography_vectors-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
********************************************
* Instructions for posting to LDAP Servers *
********************************************

%package python
Summary: python components for the cryptography_vectors package.
Group: Default

%description python
python components for the cryptography_vectors package.


%prep
%setup -q -n cryptography_vectors-1.4

%build
export LANG=C
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
