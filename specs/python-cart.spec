Name:           python-cart
Version:        1.2.3
Release:        %autorelease
Summary:        Compressed and RC4 Transport for Python

License:        MIT
URL:            https://github.com/CybercentreCanada/cart
Source:         https://github.com/CybercentreCanada/cart/archive/v%{version}/cart-%{version}.tar.gz
Patch1:         python-cart-1.2.2-cryptodomex.patch

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
This package provides Python support for CaRT (Compressed and RC4
Transport). The CaRT file format is used to store/transfer malware
and its associated metadata. It neuters the malware so it cannot be
executed and encrypts it so anti-virus software cannot flag the CaRT
file as malware.}

%description %_description

%package -n     python3-cart
Summary:        %{summary}

%description -n python3-cart %_description


%prep
%autosetup -p1 -n cart-%{version}
sed -i '/#!\/usr\/bin\/env python/d' cart/cart.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l cart


%check
%pyproject_check_import
%{py3_test_envvars} %{python3} -m unittest


%files -n python3-cart -f %{pyproject_files}
%{_bindir}/cart


%changelog
%autochangelog
