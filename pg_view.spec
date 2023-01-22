%global version_tag PG_VIEW_1_4_0
Name:           pg_view
Version:        1.4.0
Release:        12%{?dist}
Summary:        Command-line tool to display the state of the PostgreSQL processes

License:        ASL 2.0
URL:            https://github.com/zalando/pg_view
Source0:        https://github.com/zalando/pg_view/archive/%{version_tag}.tar.gz
Patch0:         pg_view-python3-shebang.patch

BuildArch:      noarch

Requires:       python3-psycopg2

%description
pg_view is a command-line tool to display the state of the PostgreSQL processes.
It shows the per-process statistics combined with pg_stat_activity output
for the processes that have the rows there, global system stats,
per-partition information and the memory stats.


%prep
%setup -qn %{name}-%{version_tag}
%patch0


%build


%install
install -D -p -m 755 %{_builddir}/%{name}-%{version_tag}/pg_view.py \
    %{buildroot}%{_bindir}/pg_view


%files
%doc CHANGELOG LICENSE README.rst images
%{_bindir}/pg_view


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 08 2017 Lorenzo Dalrio <lorenzo.dalrio@gmail.com> - 1.4.0-1
- Update to 1.4.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuild for Python 3.6

* Wed Feb 17 2016 Lorenzo Dalrio <lorenzo.dalrio@gmail.com> - 1.3.0-2
- Switch to python3 (#1308552)

* Wed Feb 10 2016 Lorenzo Dalrio <lorenzo.dalrio@gmail.com> - 1.3.0-1
- Update to 1.3.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4.20141118git11c942e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3.20141118git11c942e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 20 2014 Lorenzo Dalrio <lorenzo.dalrio@gmail.com> - 1.2.0-2.20141118git11c942e
- Patched shebang to point to /usr/bin/python2 explicitly.
- Corrected package version to reflect script version.

* Thu Nov 20 2014 Lorenzo Dalrio <lorenzo.dalrio@gmail.com> - 1.2.0-1.20141118git11c942e
- Initial release.
