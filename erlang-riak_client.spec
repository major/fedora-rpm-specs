%global realname riakc
%global upstream basho


Name:		erlang-riak_client
Version:	2.5.3
Release:	17%{?dist}
BuildArch:	noarch
Summary:	Erlang client for Riak
License:	ASL 2.0
URL:		https://github.com/%{upstream}/riak-erlang-client
VCS:		scm:git:https://github.com/%{upstream}/riak-erlang-client.git
Source0:	https://github.com/%{upstream}/riak-erlang-client/archive/%{version}/riak_client-%{version}.tar.gz
Patch1:		erlang-riak_client-0001-Allow-more-Erlang-versions.patch
Patch2:		erlang-riak_client-0002-Add-deprecation-for-Erlang-20-as-well.patch
Patch3:		erlang-riak_client-0003-Remove-excessive-export_all-directive.patch
BuildRequires:	erlang-riak_pb
BuildRequires:	erlang-rebar
Provides:	riak-erlang-client%{?_isa} = %{version}-%{release}


%description
Erlang client for Riak.


%prep
%autosetup -p1 -n riak-erlang-client-%{version}


%build
%{erlang_compile}
rebar doc -vv
rm -f edoc/edoc-info


%install
%{erlang_install}


%check
%{erlang_test}


%files
%license LICENSE
%doc README.md edoc/
%{erlang_appdir}/


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 06 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.5.3-6
- Fixed FTBFS with Erlang 20+

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.5.3-1
- Ver. 2.5.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.1.1-2
- Spec-file cleanups

* Fri Mar  4 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.1.1-1
- Ver. 2.1.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.3-1
- Ver. 1.3.3

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 10 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-1
- Ver. 1.3.1

* Wed Sep 05 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.3.0-1
- Ver. 1.3.0 (API/ABI incompatible with previous one)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 15 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-1
- Ver. 1.2.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 16 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-1
- Ver. 1.2.0

* Wed Apr 27 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.1.0-2
- Rebuild with new erlang-protobuffs

* Sat Feb 26 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.1.0-1
- Ver. 1.1.0

* Sun Jan  9 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.0.2-1
- Ver. 1.0.2

* Sat Oct 30 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.0.1-1
- Initial build

