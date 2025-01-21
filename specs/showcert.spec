Name:           showcert
Version:        0.2.12
Release:        2%{?dist}
Summary:        inspect TLS certificates presented by remote servers

License:        MIT
URL:            https://github.com/yaroslaff/showcert
Source:         %{pypi_source showcert}

BuildArch:      noarch
BuildRequires:  python3-devel


%description
Simple OpenSSL for humans: all you need for X.509 TLS certificates (and
nothing more).

showcert consist of two CLI utilities: showcert itself - all 'read' operations
with X.509 certificates and gencert - to create certificates for development
purposes.


%prep
%autosetup -p1 -n showcert-%{version}
%py3_shebang_fix showcert/gencert.py
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l showcert


%check
# upstream tests run against a couple of well-known sites, no tests
# for code so just try to run some superficial smoke tests:
%pyproject_check_import

export PATH=%{buildroot}%{_bindir}
export PYTHONPATH=%{buildroot}%{python3_sitelib}
showcert --help
gencert --help


%files -f %{pyproject_files}
%doc README.md
%{_bindir}/showcert
%{_bindir}/gencert

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Dec 28 2024 Felix Schwarz <fschwarz@fedoraproject.org> - 0.2.12-1
- update to 0.2.12

* Fri Dec 20 2024 Felix Schwarz <fschwarz@fedoraproject.org> - 0.2.11-1
- update to 0.2.11

* Sun Nov 24 2024 Felix Schwarz <fschwarz@fedoraproject.org> - 0.2.9-1
- update to 0.2.9

* Thu Aug 08 2024 Felix Schwarz <fschwarz@fedoraproject.org> - 0.2.3-1
- initial package

