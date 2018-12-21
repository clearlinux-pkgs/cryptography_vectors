#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x235AE5F129F9ED98 (paul.l.kehrer@gmail.com)
#
Name     : cryptography_vectors
Version  : 2.4.2
Release  : 62
URL      : https://files.pythonhosted.org/packages/dc/13/b502573fb34150a6cb3e146b1391f760df87d0b4fb9fd2ac23422829c8cd/cryptography_vectors-2.4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/dc/13/b502573fb34150a6cb3e146b1391f760df87d0b4fb9fd2ac23422829c8cd/cryptography_vectors-2.4.2.tar.gz
Source99 : https://files.pythonhosted.org/packages/dc/13/b502573fb34150a6cb3e146b1391f760df87d0b4fb9fd2ac23422829c8cd/cryptography_vectors-2.4.2.tar.gz.asc
Summary  : Test vectors for the cryptography package.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: cryptography_vectors-license = %{version}-%{release}
Requires: cryptography_vectors-python = %{version}-%{release}
Requires: cryptography_vectors-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
********************************************
* Instructions for posting to LDAP Servers *
********************************************

%package license
Summary: license components for the cryptography_vectors package.
Group: Default

%description license
license components for the cryptography_vectors package.


%package python
Summary: python components for the cryptography_vectors package.
Group: Default
Requires: cryptography_vectors-python3 = %{version}-%{release}

%description python
python components for the cryptography_vectors package.


%package python3
Summary: python3 components for the cryptography_vectors package.
Group: Default
Requires: python3-core

%description python3
python3 components for the cryptography_vectors package.


%prep
%setup -q -n cryptography_vectors-2.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545402621
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cryptography_vectors
cp LICENSE.APACHE %{buildroot}/usr/share/package-licenses/cryptography_vectors/LICENSE.APACHE
cp LICENSE.BSD %{buildroot}/usr/share/package-licenses/cryptography_vectors/LICENSE.BSD
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cryptography_vectors/LICENSE.APACHE
/usr/share/package-licenses/cryptography_vectors/LICENSE.BSD

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
