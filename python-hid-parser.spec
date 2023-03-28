%bcond_without check
%global pname hid-parser

Name:           python-hid-parser
Version:        0.0.3
Release:        2%{?dist}
Summary:        Parse HID report descriptors
License:        MIT
URL:            https://github.com/usb-tools/python-hid-parser
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%global _desc %{expand:
python-hid-parser is a typed pure Python library to parse HID report
descriptors.
}

%description %_desc

%package     -n python3-%{pname}
Summary:        %{summary}

%description -n python3-%{pname} %_desc

%prep
%autosetup
%generate_buildrequires
%if %{with check}
%pyproject_buildrequires -x test
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files hid_parser

%if %{with check}
%check
%pytest
%endif

%files -n python3-%{pname} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Wed Mar 08 2023 Dominik Mierzejewski <dominik@greysector.net> - 0.0.3-2
- use automatic BuildRequires generation
- conditionalize running tests

* Fri Jan 06 2023 Dominik Mierzejewski <dominik@greysector.net> - 0.0.3-1
- initial build for Fedora
