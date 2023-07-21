%global realname hyper
%global upstream GameAnalytics
%global git_tag 4b1abc4284fc784f6def4f4928f715b0d33136f9
%global short_tag %(c=%{git_tag}; echo ${c:0:7})


Name:		erlang-%{realname}
Version:	0
Release:	0.21.20161011git%{short_tag}%{?dist}
Summary:	An implementation of the HyperLogLog algorithm in Erlang
License:	MIT
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
#Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{git_tag}/%{realname}-%{version}.tar.gz
Patch1:		erlang-hyper-0001-remove-need-for-bisect-lib-hyper_bisect-as-it.patch
Patch2:		erlang-hyper-0002-Module-random-is-deprecated.patch
Patch3:		erlang-hyper-0003-Remove-unused-functions.patch
Patch4:		erlang-hyper-0004-Exclude-eunit-from-production-builds.patch
Patch5:		erlang-hyper-0005-Remove-test-failing-in-Erlang-20.patch
BuildRequires:	erlang-basho_stats
BuildRequires:	erlang-proper
BuildRequires:	erlang-rebar
BuildRequires:	erlang-stdlib2
BuildRequires:	gcc


%description
An implementation of the HyperLogLog algorithm in Erlang. Using HyperLogLog you
can estimate the cardinality of very large data sets using constant memory. The
relative error is 1.04 * sqrt(2^P). When creating a new HyperLogLog filter, you
provide the precision P, allowing you to trade memory for accuracy. The union
of two filters is lossless.


%prep
%autosetup -p1 -n %{realname}-%{git_tag}


%build
%{erlang_compile}


%install
%{erlang_install}


%check
%{erlang_test}


%files
%license LICENSE
%doc README.md
%{erlang_appdir}/


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.20161011git4b1abc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.20161011git4b1abc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20161011git4b1abc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Peter Lemenkov <lemenkov@gmail.com> - 0-0.18.20161011git4b1abc4
- Rebuild for Erlang 25

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20161011git4b1abc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20161011git4b1abc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20161011git4b1abc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20161011git4b1abc4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20161011git4b1abc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar  5 2020 Peter Lemenkov <lemenkov@gmail.com> - 0-0.12.20161011git4b1abc4
- Remove ExcludeArch for s390 - we've got a workaround fr rhbz #1770256

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20161011git4b1abc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 0-0.10.20161011git4b1abc4
- Rebuild for Erlang 22

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20161011git4b1abc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Peter Lemenkov <lemenkov@gmail.com> - 0-0.8.20161011git4b1abc4
- Rebuild with noarch deps

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20161011git4b1abc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Peter Lemenkov <lemenkov@gmail.com> - 0-0.6.20161011git4b1abc4
- Rebuild with noarch deps

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20161011git4b1abc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 0-0.4.20161011git4b1abc4
- Rebuild for Erlang 20 (with proper builddeps)

* Fri Feb 23 2018 Peter Lemenkov <lemenkov@gmail.com> - 0-0.3.20161011git4b1abc4
- Rebuild for Erlang 20

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20161011git4b1abc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 22 2017 Peter Lemenkov <lemenkov@gmail.com> - 0-0.1.20161011git4b1abc4
- Initial build

