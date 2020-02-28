#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x235AE5F129F9ED98 (paul.l.kehrer@gmail.com)
#
Name     : cryptography_vectors
Version  : 2.7
Release  : 70
URL      : https://files.pythonhosted.org/packages/d1/aa/c97197becda8c320744d76e5882b2ca54cfebc0388bb225c233555133b8d/cryptography_vectors-2.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/d1/aa/c97197becda8c320744d76e5882b2ca54cfebc0388bb225c233555133b8d/cryptography_vectors-2.7.tar.gz
Source1  : https://files.pythonhosted.org/packages/d1/aa/c97197becda8c320744d76e5882b2ca54cfebc0388bb225c233555133b8d/cryptography_vectors-2.7.tar.gz.asc
Summary  : Test vectors for the cryptography package.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: cryptography_vectors-license = %{version}-%{release}
Requires: cryptography_vectors-python = %{version}-%{release}
Requires: cryptography_vectors-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Example test files for PEM Serialization Backend tests
Contains
1. ec_private_key.pem - Contains an Elliptic Curve key generated using OpenSSL, from the curve secp256r1.
2. ec_private_key_encrypted.pem - Contains the same Elliptic Curve key as ec_private_key.pem, except that
it is encrypted with AES-256 with the password "123456".
3. ec_public_key.pem - Contains the public key corresponding to ec_private_key.pem, generated using OpenSSL.
4. rsa_private_key.pem - Contains an RSA 2048 bit key generated using OpenSSL, protected by the secret
"123456" with DES3 encryption.
5. rsa_public_key.pem - Contains an RSA 2048 bit public generated using OpenSSL from rsa_private_key.pem.
6. dsaparam.pem - Contains 2048-bit DSA parameters generated using OpenSSL; contains no keys.
7. dsa_private_key.pem - Contains a DSA 2048 bit key generated using OpenSSL from the parameters in
dsaparam.pem, protected by the secret "123456" with DES3 encryption.
8. dsa_public_key.pem - Contains a DSA 2048 bit key generated using OpenSSL from dsa_private_key.pem.

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
Provides: pypi(cryptography-vectors)

%description python3
python3 components for the cryptography_vectors package.


%prep
%setup -q -n cryptography_vectors-2.7
cd %{_builddir}/cryptography_vectors-2.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582914474
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cryptography_vectors
cp %{_builddir}/cryptography_vectors-2.7/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/cryptography_vectors/de33ead2bee64352544ce0aa9e410c0c44fdf7d9
cp %{_builddir}/cryptography_vectors-2.7/LICENSE.BSD %{buildroot}/usr/share/package-licenses/cryptography_vectors/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8
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
