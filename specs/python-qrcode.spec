# RHEL does not include pillow or pypng
%bcond extras %[%{undefined rhel} || %{defined epel}]

%global pkgname qrcode

Name:           python-%{pkgname}
Version:        8.0
Release:        %autorelease
Summary:        Python QR Code image generator

License:        BSD-3-Clause
URL:            https://github.com/lincolnloop/python-qrcode
Source0:        %{pypi_source qrcode}
Source1:        flit-pyproject.toml.in
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%description
This module uses the Python Imaging Library (PIL) to allow for the\
generation of QR Codes.


%package -n python3-%{pkgname}
Summary:        Python QR Code image generator
Obsoletes:      python3-qrcode-core < 7.4.2-2
Provides:       python3-qrcode-core = %{version}-%{release}
%if %{with extras}
Recommends:     (python3-%{pkgname}+pil or python3-%{pkgname}+png or python3-%{pkgname}+all)
%endif

%description -n python3-%{pkgname}
This module uses the Python Imaging Library (PIL) to allow for the
generation of QR Codes. Python 3 version.


%if %{with extras}
%pyproject_extras_subpkg -n python3-%{pkgname} pil,png,all
%endif


%generate_buildrequires
# RHEL does not include the extra test dependencies (coverage, pillow)
%pyproject_buildrequires %{?with_extras:-x pil -x png}


%prep
%autosetup -n qrcode-%{version} -p1
# Remove shebang
sed -i '1d' qrcode/console_scripts.py
%if %{defined rhel} && %{undefined epel}
# use flit-core instead of poetry-core
sed -e 's|@VERSION@|%{version}|' %{SOURCE1} > pyproject.toml
%endif


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files qrcode


%check
%pytest -v


%files -n python3-%{pkgname} -f %{pyproject_files}
%doc README.rst CHANGES.rst
%license LICENSE
%{_bindir}/qr


%changelog
%autochangelog
