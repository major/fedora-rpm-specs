Name:           python-icmplib
Version:        3.0.3
Release:        %autorelease
Summary:        An implementation of the ICMP protocol in Python
# See https://github.com/ValentinBELYN/icmplib/issues/72
License:        LGPL-3.0-or-later
URL:            https://github.com/ValentinBELYN/icmplib
# pypi_source tar ball differs from github tag and is lacking docs/examples :(
Source:         https://github.com/ValentinBELYN/icmplib/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
An implementation of the ICMP protocol in Python.}

%description %_description

%package -n     python3-icmplib
Summary:        %{summary}

%description -n python3-icmplib %_description

%prep
%autosetup -p1 -n icmplib-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files icmplib

%check
%pyproject_check_import

%files -n python3-icmplib -f %{pyproject_files}
%license LICENSE
%doc docs/* examples/*.py

%changelog
%autochangelog
