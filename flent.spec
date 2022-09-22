%global srcname flent

Name:             flent
Version:          2.0.1
Release:          7%{?dist}
Summary:          FLExible Network Tester for bufferbloat testing and more

License:          GPLv3+
URL:              https://flent.org/
Source0:          %{pypi_source}

BuildArch:        noarch
BuildRequires:    python3-devel python3-mock python3-sphinx desktop-file-utils libappstream-glib python3-setuptools make
Recommends:       python3-matplotlib python3-matplotlib-qt5 python3-pyside2 python3-qtpy
Requires:         fping netperf golang-github-heistp-irtt

%description
The FLExible Network Tester is a Python wrapper to run multiple simultaneous
netperf/iperf/ping instances and aggregate the results.

Tests are specified as config files (which are really Python), and
various parsers for tool output are supplied. At the moment, parsers for
netperf in -D mode, iperf in csv mode and ping/ping6 in -D mode are
supplied, as well as a generic parser for commands that just outputs a
single number.

Several commands can be run in parallel and, provided they output
timestamped values, (which netperf ping and iperf do, the latter with a
small patch, available in the misc/ directory), the test data points can
be aligned with each other in time, interpolating differences between
the actual measurement points. This makes it possible to graph (e.g.)
ping times before, during and after a link is loaded.

%package doc
Summary:          Documentation for Flent: The FLExible Network Tester
BuildArch:        noarch

%description doc
Documentation for users of The FLExible Network Tester

The FLExible Network Tester is a Python wrapper to run multiple simultaneous
netperf/iperf/ping instances and aggregate the results.

Tests are specified as config files (which are really Python), and
various parsers for tool output are supplied. At the moment, parsers for
netperf in -D mode, iperf in csv mode and ping/ping6 in -D mode are
supplied, as well as a generic parser for commands that just outputs a
single number.

Several commands can be run in parallel and, provided they output
timestamped values, (which netperf ping and iperf do, the latter with a
small patch, available in the misc/ directory), the test data points can
be aligned with each other in time, interpolating differences between
the actual measurement points. This makes it possible to graph (e.g.)
ping times before, during and after a link is loaded.

%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build
%make_build -C doc/ html PYTHON=%{__python3} SPHINXBUILD=sphinx-build-3
rm -f doc/_build/html/index.html doc/_build/html/.buildinfo

%install
%py3_install

%check
%make_build test PYTHON=%{__python3}
desktop-file-validate %{buildroot}/%{_datadir}/applications/flent.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files
%{python3_sitelib}/flent
%{python3_sitelib}/%{srcname}-*.egg-info/
%{_bindir}/flent
%{_bindir}/flent-gui
%{_datadir}/applications/flent.desktop
%{_datadir}/mime/packages/flent-mime.xml
%{_metainfodir}/flent.appdata.xml
%{_mandir}/man1/flent.1.gz
%doc README.rst CHANGES.md BUGS batchfile.example flentrc.example flent-paper.batch misc/
%license LICENSE

%files doc
%doc doc/_build/html

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.1-6
- Rebuilt for Python 3.11

* Mon Jun 6 2022 Toke Høiland-Jørgensen <toke@toke.dk> - 2.0.1-5
- Add missing python3-matplotlib-qt5 dependency (fedora#2093515)

* Fri May 13 2022 Toke Høiland-Jørgensen <toke@toke.dk> - 2.0.1-4
- Add fping, irtt and netperf dependencies, switch to pyside2 for Qt dep.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 24 2021 Toke Høiland-Jørgensen <toke@toke.dk> 2.0.1-1
- Upstream release 2.0.1

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Toke Høiland-Jørgensen <toke@toke.dk> 2.0.0-1
- Upstream release 2.0.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Toke Høiland-Jørgensen <toke@toke.dk> 1.3.2-4
- Add python3-setuptools to BuildRequires

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Toke Høiland-Jørgensen <toke@toke.dk> 1.3.2-1
- Upstream release 1.3.2

* Tue Nov 26 2019 Toke Høiland-Jørgensen <toke@toke.dk> 1.3.1-1
- Upstream release 1.3.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul  9 2019 Toke Høiland-Jørgensen <toke@toke.dk> 1.3.0-1
- Upstream release 1.3.0

* Mon Jul 8 2019 Toke Høiland-Jørgensen <toke@redhat.com> 1.2.2-1
- Initial release
