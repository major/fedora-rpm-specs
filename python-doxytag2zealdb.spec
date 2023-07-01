%global shortname doxytag2zealdb

%global descrip \
doxytag2zealdb creates a SQLite3 database from a Doxygen tag file to enable\
searchable Doxygen docsets with categorized entries in tools like helm-dash,\
Zeal, and Dash.

Name:           python-%{shortname}
Version:        0.3.1
Release:        8%{?dist}
Summary:        Create a SQLite3 database from a Doxygen tag file

License:        GPLv3+
URL:            https://gitlab.com/vedvyas/doxytag2zealdb
Source0:        https://gitlab.com/vedvyas/doxytag2zealdb/-/archive/v%{version}/%{shortname}-v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel >= 3.6
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(docopt) >= 0.6.2
BuildRequires:  python3dist(lxml) >= 3.6.0
BuildRequires:  python3dist(beautifulsoup4) >= 4.4.1
BuildRequires:  python3dist(future)

%description    %{descrip}



%package -n %{shortname}
Summary:  %{summary}
Requires: python3-%{shortname} = %{version}-%{release}

%description -n %{shortname}
%{descrip}



%package -n python3-%{shortname}
Summary:    Python modules for git-revise
Recommends: %{shortname} = %{version}-%{release}

%description -n python3-%{shortname}
This package contains the python modules for the doxytag2zealdb program.



%prep
%autosetup -n %{shortname}-v%{version}


%build
%py3_build


%install
%py3_install

# Fixup the script's executable features
chmod +x %{buildroot}%{python3_sitelib}/%{shortname}/doxytag2zealdb.py
%py3_shebang_fix %{buildroot}%{python3_sitelib}/%{shortname}/doxytag2zealdb.py


%files -n %{shortname}
%license COPYING
%doc CONTRIBUTORS
%doc README.md
%{_bindir}/doxytag2zealdb

%files -n python3-%{shortname}
%license COPYING
%doc CONTRIBUTORS
%doc README.md
%{python3_sitelib}/%{shortname}
%{python3_sitelib}/%{shortname}-%{version}-py%{python3_version}.egg-info



%changelog
* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.3.1-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.1-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.1-2
- Rebuilt for Python 3.10

* Wed Apr 14 2021 Ian McInerney <ian.s.mcinerney@ieee.org> - 0.3.1-1
- Initial package.
