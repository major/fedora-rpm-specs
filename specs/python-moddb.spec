Name:           python-moddb
Version:        0.12.0
Release:        2%{?dist}
Summary:        A Python scraper/parser for ModDB
License:        MIT
URL:            https://github.com/ClementJ18/moddb
Source0:        %{url}/archive/v%{version}/moddb-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
%global _description %{expand:
                       The goal of the library is to be able to navigate ModDB purely
                       programmatically through scraping and parsing of the various models
                       present on the website. This is based off a command of a bot which
                       can parse either a game or a mod, this command gave birth to the
                       original library which was extremely limited in its abilities and
                       only able to parse a few pages with inconsistencies. This library
                       is a much more mature and professional attempt at the whole idea,
                       adding on a much deeper understanding of OOP.}


%description %{_description}


%package -n python3-moddb
Summary:        %{summary}


%description -n python3-moddb %{_description}


%prep
%autosetup -p1 -n moddb-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files moddb


%check
# Upstream tests generally require network access and authentication
%pyproject_check_import

%files -n python3-moddb -f %{pyproject_files}
%doc README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.11.0-2
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.8.1-2
- Rebuilt for Python 3.12

* Tue Feb 14 2023 Steve Cossette <farchord@gmail.com> and Chris King <bunnyapocalypse@protonmail.com> - 0.8.1-1
- Initial release of moddb (0.8.1)
