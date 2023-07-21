%global realname bitcask
%global upstream basho


Name:		erlang-%{realname}
Version:	2.1.0
Release:	10%{?dist}
Summary:	Eric Brewer-inspired key/value store
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Source1:	bitcask.licensing
Patch1:		erlang-bitcask-0001-Don-t-use-deprecated-erlang-now-0.patch
Patch2:		erlang-bitcask-0002-Remove-eqc-we-still-don-t-use-them.patch
Patch3:		erlang-bitcask-0003-Remove-pc-target.patch
BuildRequires:	erlang-cuttlefish
BuildRequires:	erlang-meck
BuildRequires:	erlang-rebar3
BuildRequires:	gcc


%description
Eric Brewer-inspired key/value store.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang3_compile}

# FIXME we don't have a port compiler plugin for rebar3 yet
mkdir -p priv
gcc $CFLAGS -c -I%{_libdir}/erlang/usr/include c_src/bitcask_nifs.c -o c_src/bitcask_nifs.o
gcc $CFLAGS -c -I%{_libdir}/erlang/usr/include c_src/erl_nif_util.c -o c_src/erl_nif_util.o
gcc $CFLAGS -c -I%{_libdir}/erlang/usr/include c_src/murmurhash.c -o c_src/murmurhash.o
gcc $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei c_src/bitcask_nifs.o c_src/erl_nif_util.o c_src/murmurhash.o -o priv/bitcask.so

%install
%{erlang3_install}

cp -arv priv/bitcask.schema %{buildroot}%{erlang_appdir}/priv
cp -arv priv/bitcask_multi.schema %{buildroot}%{erlang_appdir}/priv


%check
%{erlang3_test}


%files
%doc README.md THANKS doc/
%{erlang_appdir}/


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Peter Lemenkov <lemenkov@gmail.com> - 2.1.0-8
- Fix FTBFS with rebar3

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Peter Lemenkov <lemenkov@gmail.com> - 2.1.0-6
- Rebuild for Erlang 25

* Thu Feb 17 2022 Peter Lemenkov <lemenkov@gmail.com> - 2.1.0-5
- Switch to rebar3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  2 2020 Peter Lemenkov <lemenkov@gmail.com> - 2.1.0-1
- Ver. 2.1.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.0.8-10
- Rebuild for Erlang 22

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.0.8-6
- Rebuild for Erlang 20 (with proper builddeps)

* Fri Feb 23 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.0.8-5
- Rebuild for Erlang 20

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar  8 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.0.8-1
- Ver. 2.0.8

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.0.7-1
- Ver. 2.0.7

* Thu Oct 20 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.0.6-1
- Ver. 2.0.6

* Tue Aug 16 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.0.3-1
- Ver. 2.0.3
- Fixed FTBFS with Erlang 19

* Sun Aug 07 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.7.4-3
- Rebuild for Erlang 19

* Sun May  8 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.7.4-2
- Remove bogus runtime dependency - eunit

* Sun Apr 17 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.7.4-1
- Ver. 1.7.4

* Fri Apr 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.6.1-11
- Drop unneeded macro

* Sat Apr  2 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.6.3-10
- Rebuild with Erlang 18.3

* Fri Feb 12 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.6.3-9
- Fixed FTBFS in Rawhide

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 04 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.6.3-6
- Rebuild with Erlang 17.3.3

* Thu Aug 28 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.6.3-5
- Rebuild with Erlang 17.2.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.6.3-3
- Use new erlang macros to build with $RPM_OPT/LD_FLAGS etc, verbosely

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jul 31 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.6.3-1
- Ver. 1.6.3

* Sun Apr 07 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.6.1-1
- Ver. 1.6.1

* Sun Mar 10 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-1
- Ver. 1.6.0
- Fix FTBFS in Rawhide (F19)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 11 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.5.2-1
- Ver. 1.5.2 (Bugfix release)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.5.1-2
- Require specific %%{_isa} to avoid multiarch issues

* Thu May 17 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.5.1-1
- Ver. 1.5.1

* Fri Sep 16 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-1
- Ver. 1.2.0

* Fri Jan 14 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.1.5-1
- Ver. 1.1.5
- Pass optflags to C-compiler

* Fri Nov 12 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.1.4-1
- Initial build

