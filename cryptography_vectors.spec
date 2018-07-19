#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x235AE5F129F9ED98 (paul.l.kehrer@gmail.com)
#
Name     : cryptography_vectors
Version  : 2.3
Release  : 59
URL      : http://pypi.debian.net/cryptography_vectors/cryptography_vectors-2.3.tar.gz
Source0  : http://pypi.debian.net/cryptography_vectors/cryptography_vectors-2.3.tar.gz
Source99 : http://pypi.debian.net/cryptography_vectors/cryptography_vectors-2.3.tar.gz.asc
Summary  : Test vectors for the cryptography package.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: cryptography_vectors-python3
Requires: cryptography_vectors-license
Requires: cryptography_vectors-python
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
This zip file contains sample test vectors (values) for the following functions defined in
NIST SP 800-38F:

%package license
Summary: license components for the cryptography_vectors package.
Group: Default

%description license
license components for the cryptography_vectors package.


%package python
Summary: python components for the cryptography_vectors package.
Group: Default
Requires: cryptography_vectors-python3

%description python
python components for the cryptography_vectors package.


%package python3
Summary: python3 components for the cryptography_vectors package.
Group: Default
Requires: python3-core

%description python3
python3 components for the cryptography_vectors package.


%prep
%setup -q -n cryptography_vectors-2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532005886
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/cryptography_vectors
cp LICENSE.BSD %{buildroot}/usr/share/doc/cryptography_vectors/LICENSE.BSD
cp LICENSE.APACHE %{buildroot}/usr/share/doc/cryptography_vectors/LICENSE.APACHE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/cryptography_vectors/LICENSE.APACHE
/usr/share/doc/cryptography_vectors/LICENSE.BSD

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
