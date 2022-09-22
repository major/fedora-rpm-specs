%global srcname rq

Name:           python-%{srcname}
Version:        1.7.0
Release:        8%{?dist}
Summary:        Simple, lightweight, library for creating background jobs, and processing them

License:        BSD
URL:            https://github.com/rq/rq
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
RQ (Redis Queue) is a simple Python library for queueing jobs
and processing them in the background with workers.
It is backed by Redis and it is designed to have a low barrier to entry.
It should be integrated in your web stack easily.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%files -n python3-%{srcname} -f %pyproject_files
%license LICENSE
%doc README.md
%{_bindir}/rq
%{_bindir}/rqinfo
%{_bindir}/rqworker

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.7.0-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.7.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 15 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.7.0-2
- Convert to pyproject macros

* Sat Dec 12 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Initial package
