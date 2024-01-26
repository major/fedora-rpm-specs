Name:		erlang-rpm-macros
Version:	0.3.6
Release:	6%{?dist}
Summary:	Macros for simplifying building of Erlang packages
License:	MIT
URL:		https://github.com/fedora-erlang/erlang-rpm-macros
VCS:		scm:git:https://github.com/fedora-erlang/erlang-rpm-macros.git
Source0:	https://github.com/fedora-erlang/erlang-rpm-macros/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
# These BRs needed only for testing
BuildRequires:	erlang-crypto
BuildRequires:	erlang-erlsyslog
BuildRequires:	erlang-erts
BuildRequires:	python3-pybeam
BuildRequires:	python3-pyelftools
BuildRequires:	python3-rpm
BuildRequires: make
Requires:	rpm-build >= 4.11
# Requires for BEAM parsing
Requires:	python3-pybeam
# Requires for so-lib parsing
Requires:	python3-pyelftools
Requires:	python3-rpm


%description
Macros for simplifying building of Erlang packages.


%prep
%autosetup -p1


%build
# Nothing to build


%install
install -d %{buildroot}%{_rpmconfigdir}/fileattrs
install -d %{buildroot}%{_rpmconfigdir}/macros.d
install -p -m 0755 erlang-find-provides.py %{buildroot}%{_rpmconfigdir}/erlang-find-provides
install -p -m 0755 erlang-find-requires.py %{buildroot}%{_rpmconfigdir}/erlang-find-requires
install -p -m 0644 macros.erlang %{buildroot}%{_rpmconfigdir}/macros.d/
install -p -m 0644 erlang.attr %{buildroot}%{_rpmconfigdir}/fileattrs/


%check
make check


%files
%license LICENSE
%doc README
%{_rpmconfigdir}/erlang-find-provides
%{_rpmconfigdir}/erlang-find-requires
%{_rpmconfigdir}/fileattrs/erlang.attr
%{_rpmconfigdir}/macros.d/macros.erlang


%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 17 2022 Peter Lemenkov <lemenkov@gmail.com> - 0.3.6-1
- Ver. 0.3.6

* Thu Feb 17 2022 Peter Lemenkov <lemenkov@gmail.com> - 0.3.5-1
- Ver. 0.3.5

* Mon Feb  7 2022 Peter Lemenkov <lemenkov@gmail.com> - 0.3.4-1
- Ver. 0.3.4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov  9 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.3.3-1
- Ver. 0.3.3

* Fri Nov  8 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.3.2-1
- Ver. 0.3.2

* Fri Aug 30 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.3.1-1
- Ver. 0.3.1

* Fri Aug 30 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.3.0-1
- Ver. 0.3.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Peter Lemenkov <lemenkov@gmail.com> - 0.2.9-3
- Fix FTBFS in Rawhide

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 13 2018 Peter Lemenkov <lemenkov@gmail.com> - 0.2.9-1
- Ver. 0.2.9

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.2.8-1
- Ver. 0.2.8

* Mon May 22 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.2.7-1
- Ver. 0.2.7

* Wed May 17 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.2.5-1
- Ver. 0.2.5

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-2
- Rebuild for Python 3.6

* Thu Sep  1 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.2.4-1
- Ver. 0.2.4

* Thu May 12 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.2.3-1
- Ver. 0.2.3
- Switch to Python3

* Thu Mar 10 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.2.2-1
- Ver. 0.2.2

* Mon Mar  7 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.2.1-2
- Allow skippind dependency checking in rebar

* Sun Mar  6 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.2.1-1
- Ver. 0.2.1

* Tue Mar  1 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.2.0-2
- Added missing Requires

* Tue Mar  1 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.2.0-1
- Ver. 0.2.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 13 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.1.4-1
- Ver. 0.1.4
- Dropped support for pre-4.11 rpms (EL7 or Fedora is required)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 31 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.1.3-6
- Cleaning up spec-file

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.1.3-4
- Remove %%config from %%{_sysconfdir}/rpm/macros.*
  (https://fedorahosted.org/fpc/ticket/259).

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 07 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.1.3-1
- Ver. 0.1.3

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.1.2-2
- Drop explicit Requires: erlang-erts

* Mon Nov 15 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.1.2-1
- Ver. 0.1.2
- Added missing runtime requirements

* Wed Oct 27 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.1.1-1
- Initial build as separate package (splitted off from erlang)
