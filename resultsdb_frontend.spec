Name:           resultsdb_frontend
# NOTE: if you update version, *make sure* to also update `resultsdb_frontend/__init__.py`
Version:        2.1.2
Release:        13%{?dist}
Summary:        Frontend for the ResultsDB

License:        GPLv2+
URL:            https://pagure.io/taskotron/resultsdb_frontend
Source0:        https://qa.fedoraproject.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python3-flask
Requires:       python3-iso8601
Requires:       python3-resultsdb_api
Requires:       python3-six
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
ResultsDB fronted is a simple application that
allows browsing the data stored inside ResultsDB.

%prep
%setup -q

%check
# for some reason, this is the only place where the files get deleted, better ideas?
rm -f %{buildroot}%{_sysconfdir}/resultsdb_frontend/*.py{c,o}

%build
%py3_build

%install
%py3_install

# apache and wsgi settings
mkdir -p %{buildroot}%{_datadir}/resultsdb_frontend/conf
install -p -m 0644 conf/resultsdb_frontend.conf %{buildroot}%{_datadir}/resultsdb_frontend/conf/resultsdb_frontend.conf
install -p -m 0644 conf/resultsdb_frontend.wsgi %{buildroot}%{_datadir}/resultsdb_frontend/resultsdb_frontend.wsgi

mkdir -p %{buildroot}%{_sysconfdir}/resultsdb_frontend
install -p -m 0644 conf/settings.py.example %{buildroot}%{_sysconfdir}/resultsdb_frontend/settings.py

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/resultsdb_frontend
%{python3_sitelib}/*.egg-info

%dir %{_sysconfdir}/resultsdb_frontend
%config(noreplace) %{_sysconfdir}/resultsdb_frontend/settings.py

%dir %{_datadir}/resultsdb_frontend
%{_datadir}/resultsdb_frontend/*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.2-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.2-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.1.2-1
- Fix default search doesn't show today's results

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.1.1-1
- Use Python 3
- Limit searches by time by default and setting in the search UI
- Handle exceptions from resultdb_api gracefully

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.1.0-1
- Fix default wildcard search in frontend (100x spedup)
- Improve experience when an optional parameter is not defined on results

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Kamil Páral <kparal@redhat.com> - 2.0.0-1
- remove flask-restful dependency
- fix testcase info links
- point default config to resultsdb 2.0 API
- fix search box
- synchronize major version number with resultsdb major number

* Thu Nov 10 2016 Martin Krizek <mkrizek@fedoraproject.org> - 1.2.0-2
- do not replace config file

* Thu Nov 3 2016 Tim FLink <tflink@fedoraproject.org> - 1.2.0-1
- add support for resultsdb v2.0

* Mon Sep 26 2016 Martin Krizek <mkrizek@redhat.com> - 1.1.9-4
- preserve timestamps on installed files

* Wed Sep 21 2016 Martin Krizek <mkrizek@redhat.com> - 1.1.9-3
- use python macros for building and installing
- use python2-* where possible

* Mon Jun 13 2016 Martin Krizek <mkrizek@redhat.com> - 1.1.9-2
- add license
- remove not needed custom macros

* Thu Dec 17 2015 Martin Krizek <mkrizek@redhat.com> - 1.1.9-1
- cleaner search with no item specified (D566)
- change mock root to f22

* Tue Aug 18 2015 Tim Flink <tflink@fedoraproject.org> - 1.1.8-1
- add fedmenu support (D363)

* Wed Jul 22 2015 Martin Krizek <mkrizek@redhat.com> - 1.1.7-1
- provide better description of the job info link

* Tue Jul 21 2015 Martin Krizek <mkrizek@redhat.com> - 1.1.6-1
- firefox search fix
- search by outcome

* Wed Jul 8 2015 Martin Krizek <mkrizek@redhat.com> - 1.1.5-1
- Search improvements
- Updated conf to be compatible with Apache 2.4
- Show version in footer

* Wed Apr 1 2015 Tim Flink <tflink@fedoraproject.org> - 1.1.4-1
- better handling of 404 errors (T410)
- fixing search button to redirect to proper URL (T402)

* Wed Oct 29 2014 Tim Flink <tflink@fedoraproject.org> - 1.1.3-1
- adding search button to frontpage (T347)

* Fri Jun 27 2014 Tim Flink <tflink@fedoraproject.org> - 1.1.1-1
- Adding link to logs from result detail

* Fri May 16 2014 Tim Flink <tflink@fedoraproject.org> - 1.1.0-1
- Releasing resultsdb_frontend 1.1.0

* Fri Apr 25 2014 Tim Flink <tflink@fedoraproject.org> - 1.0.2-1
- updating to new upstream, fixing some variable name errors

* Fri Apr 25 2014 Tim Flink <tflink@fedoraproject.org> - 1.0.1-2
- updating to new upstream, fixing resultsdb_api dep, removing resultsdb_frontend binary

* Thu Feb 6 2014 Jan Sedlak <jsedlak@redhat.com> - 1.0.0-1
- initial packaging
