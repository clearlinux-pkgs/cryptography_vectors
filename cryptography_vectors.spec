#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x235AE5F129F9ED98 (paul.l.kehrer@gmail.com)
#
Name     : cryptography_vectors
Version  : 3.4.7
Release  : 89
URL      : https://files.pythonhosted.org/packages/31/4e/c65f43cb4d05ed3637a3bf3a0c28c7f2426781950f65b0f350fd7d268a35/cryptography_vectors-3.4.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/31/4e/c65f43cb4d05ed3637a3bf3a0c28c7f2426781950f65b0f350fd7d268a35/cryptography_vectors-3.4.7.tar.gz
Source1  : https://files.pythonhosted.org/packages/31/4e/c65f43cb4d05ed3637a3bf3a0c28c7f2426781950f65b0f350fd7d268a35/cryptography_vectors-3.4.7.tar.gz.asc
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
Provides: pypi(cryptography_vectors)

%description python3
python3 components for the cryptography_vectors package.


%prep
%setup -q -n cryptography_vectors-3.4.7
cd %{_builddir}/cryptography_vectors-3.4.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622654175
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cryptography_vectors
cp %{_builddir}/cryptography_vectors-3.4.7/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/cryptography_vectors/de33ead2bee64352544ce0aa9e410c0c44fdf7d9
cp %{_builddir}/cryptography_vectors-3.4.7/LICENSE.BSD %{buildroot}/usr/share/package-licenses/cryptography_vectors/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cryptography_vectors/de33ead2bee64352544ce0aa9e410c0c44fdf7d9
/usr/share/package-licenses/cryptography_vectors/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
