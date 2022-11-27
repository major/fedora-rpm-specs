%global pkgname qrcode

Name:           python-%{pkgname}
Version:        7.3.1
Release:        %autorelease
Summary:        Python QR Code image generator

License:        BSD
URL:            https://github.com/lincolnloop/python-qrcode
Source0:        https://pypi.python.org/packages/source/q/qrcode/qrcode-%{version}.tar.gz
# skip all PIL-dependent tests on RHEL
Patch0:         qrcode-7.3.1-image-tests.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
%if ! 0%{?rhel}
# RHEL only ships qrcode-core and does not have pillow
BuildRequires:  python3-imaging
%endif

%global _description\
This module uses the Python Imaging Library (PIL) to allow for the\
generation of QR Codes.

%description %_description

%package -n python3-%{pkgname}
Summary:        Python QR Code image generator
Requires:       python3-imaging
# For entry point:
Requires:       python3-setuptools
Requires:       python3-%{pkgname}-core = %{version}-%{release}

%description -n python3-%{pkgname}
This module uses the Python Imaging Library (PIL) to allow for the
generation of QR Codes. Python 3 version.

%package -n python3-%{pkgname}-core
Requires:       python3-six
Summary:        Python 3 QR Code image generator (core library)

%description -n python3-%{pkgname}-core
Core Python 3 module for QR code generation. Does not contain image rendering.

%prep
%autosetup -n qrcode-%{version} -p1

# The pure plugin requires pymaging which is not packaged in Fedora.
rm qrcode/image/pure.py*

# Remove shebang
sed -i '1d' qrcode/console_scripts.py

%build
%py3_build

%install
%py3_install

# Do not install tests
rm -r %{buildroot}%{python3_sitelib}/%{pkgname}/tests

#
# In previous iterations of the package, the qr script had been
# renamed to qrcode. This was an unnecessary change from upstream.
#
# We cary this symlink to maintain compat with old packages.
#
ln -s qr %{buildroot}%{_bindir}/qrcode

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    %{__python3} -m unittest -v qrcode.tests.test_qrcode.QRCodeTests

%files -n python3-%{pkgname}
%{_bindir}/qr
%{_bindir}/qrcode
%{_mandir}/man1/qr.1*
%{python3_sitelib}/%{pkgname}/image/svg.py*
%{python3_sitelib}/%{pkgname}/image/pil.py*
%{python3_sitelib}/%{pkgname}/image/styledpil.py*
%{python3_sitelib}/%{pkgname}/image/__pycache__/svg.*
%{python3_sitelib}/%{pkgname}/image/__pycache__/pil.*
%{python3_sitelib}/%{pkgname}/image/__pycache__/styledpil.*

%files -n python3-%{pkgname}-core
%doc README.rst CHANGES.rst
%license LICENSE
%dir %{python3_sitelib}/%{pkgname}/
%dir %{python3_sitelib}/%{pkgname}/image
%dir %{python3_sitelib}/%{pkgname}/image/__pycache__
%{python3_sitelib}/%{pkgname}*.egg-info
%{python3_sitelib}/%{pkgname}/*.py*
%{python3_sitelib}/%{pkgname}/__pycache__
%{python3_sitelib}/%{pkgname}/image/__init__.py*
%{python3_sitelib}/%{pkgname}/image/base.py*
%{python3_sitelib}/%{pkgname}/image/styles/
%{python3_sitelib}/%{pkgname}/image/__pycache__/__init__.*
%{python3_sitelib}/%{pkgname}/image/__pycache__/base.*

%changelog
%autochangelog
