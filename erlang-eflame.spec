%global realname eflame
%global upstream slfritchie


Name:		erlang-%{realname}
Version:	0
Release:	0.30.gita085181%{?dist}
BuildArch:	noarch
Summary:	Flame Graph profiler for Erlang
License:	MIT
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
#Source0:	https://github.com/%%{upstream}/%%{realname}/archive/%%{version}/%%{realname}-%%{version}.tar.gz
Source0:	https://github.com/%{upstream}/%{realname}/archive/a08518142126f5fc541a3a3c4a04c27f24448bae/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar
BuildRequires:	perl-generators


%description
Flame Graph profiler for Erlang.


%prep
%setup -q -n %{realname}-a08518142126f5fc541a3a3c4a04c27f24448bae


%build
%{erlang_compile}


%install
%{erlang_install}

install -D -p -m 0755 flamegraph.pl %{buildroot}%{erlang_appdir}/bin/flamegraph.pl
install -D -p -m 0755 flamegraph.riak-color.pl %{buildroot}%{erlang_appdir}/bin/flamegraph.riak-color.pl


%check
%{erlang_test}


%files
%license LICENSE
%doc README.md README-Riak-Example.md
%{erlang_appdir}/


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.30.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.28.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0-0.27.gita085181
- Perl 5.36 re-rebuild of bootstrapped packages

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0-0.26.gita085181
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 27 2021 Peter Lemenkov <lemenkov@gmail.com> - 0-0.23.gita085181
- Rebuild

* Thu May 27 2021 Peter Lemenkov <lemenkov@gmail.com> - 0-0.22.gita085181
- Rebootstrap erlang-eflame with new Perl

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0-0.21.gita085181
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0-0.18.gita085181
- Perl 5.32 rebuilt after bootstrapping

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0-0.17.gita085181
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 10 2019 Peter Lemenkov <lemenkov@gmail.com> - 0-0.15.gita085181
- Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Peter Lemenkov <lemenkov@gmail.com> - 0-0.13.gita085181
- Perl 5.30 rebuild (2)

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0-0.12.gita085181
- Perl 5.30 rebuild

* Wed Feb 27 2019 Peter Lemenkov <lemenkov@gmail.com> - 0-0.11.gita085181
- Switch to noarch

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0-0.8.gita085181
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0-0.4.gita085181
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0-0.2.gita085181
- Perl 5.24 rebuild

* Fri Apr 22 2016 Peter Lemenkov <lemenkov@gmail.com> - 0-0.1.gita085181
- Initial build

