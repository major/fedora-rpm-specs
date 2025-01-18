%global realname riak_kv
%global upstream basho


Name:		erlang-%{realname}
Version:	2.1.8
Release:	22%{?dist}
BuildArch:	noarch
Summary:	Riak Key/Value Store
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:	Apache-2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-riak_kv-0001-Don-t-use-obsolete-erlang-now-0.patch
Patch2:		erlang-riak_kv-0002-Disable-fancy-eunit-output.patch
Patch3:		erlang-riak_kv-0003-New-lager-API.patch
Patch4:		erlang-riak_kv-0004-Proper-place-for-schemas.patch
Patch5:		erlang-riak_kv-0005-Don-t-use-deps-for-schema-files-when-testing.patch
Patch6:		erlang-riak_kv-0006-Use-system-wide-mochiweb.patch
Patch7:		erlang-riak_kv-0007-Don-t-use-deprecated-module-random.patch
Patch8:		erlang-riak_kv-0008-Export-missing-type-when-necessary.patch
Patch9:		erlang-riak_kv-0009-Don-t-use-obsolete-crypto-functions.patch
Patch10:	erlang-riak_kv-0010-Don-t-threat-warnings-as-errors.patch
Patch11:	erlang-riak_kv-0011-Erlang_js-is-no-longer-an-application.patch
Patch12:	erlang-riak_kv-0012-Load-cuttlefish-schemas-from-noarch-dir-as-well.patch
Patch13:	erlang-riak_kv-0013-Fix-common_tests-suite.patch
BuildRequires:	erlang-bitcask
BuildRequires:	erlang-chronos
BuildRequires:	erlang-clique
BuildRequires:	erlang-eper
BuildRequires:	erlang-hyper
BuildRequires:	erlang-js
BuildRequires:	erlang-meck
BuildRequires:	erlang-rebar
BuildRequires:	erlang-riak_api
BuildRequires:	erlang-riak_dt
BuildRequires:	erlang-riak_pipe
BuildRequires:	erlang-sext
BuildRequires:	erlang-sidejob


%description
Riak Key/Value Store.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}

install -D -p -m 0644 priv/mapred_builtins.js %{buildroot}%{erlang_appdir}/priv/mapred_builtins.js
install -D -p -m 0644 priv/riak_kv.schema %{buildroot}%{erlang_appdir}/priv/riak_kv.schema
install -D -p -m 0644 priv/multi_backend.schema %{buildroot}%{erlang_appdir}/priv/multi_backend.schema


%check
%{erlang_test}


%files
%doc docs/* README.org
%{erlang_appdir}/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.8-21
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.1.8-10
- Rebuilt with fixed Rebar

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.1.8-7
- Fixed common_tests suite

* Thu Sep 13 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.1.8-6
- Really fix FTBFS with Erlang 20+

* Thu Sep 06 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.1.8-5
- Fix FTBFS with Erlang 20+
- Switch to noarch

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.1.8-3
- Fix FTBFS with Erlang 20
- Rebuild for Erlang 20 (with proper builddeps)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 21 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.1.8-1
- Ver. 2.1.8

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.1.2-2
- Install schemas properly

* Fri Apr 22 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.1.2-1
- Ver. 2.1.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1.3.2-5
- Patch to get it built with erlang-js 1.3.0 and erlang-ebloom 2.0.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.2-1
- Ver. 1.3.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 24 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-1
- Ver. 1.3.1

* Mon Mar 11 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.0-1
- Ver. 1.3.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3.p3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 18 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-2.p3
- Ver. 1.2.1p3

* Sat Oct 27 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-1.p2
- Ver. 1.2.1p2

* Sun Aug 05 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.4-1
- Ver. 1.1.4 (security bugfix)

* Tue Jun 19 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.2-1
- Ver. 1.1.2

* Sat Feb 26 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.14.1-1
- Ver. 0.14.1

* Sun Jan 23 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.14.0-1
- Ver. 0.14.0

* Fri Nov 12 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.13.0-1
- Initial build

