%global realname rebar
%global upstream rebar

# Set this to true when starting a rebuild of the whole erlang stack. There's
# a cyclical dependency between erlang-rebar and erlang-getopt so this package
# (rebar) needs to get built first in bootstrap mode.
%global need_bootstrap_set 0

%{!?need_bootstrap: %global need_bootstrap  %{need_bootstrap_set}}


Name:		erlang-%{realname}
Version:	2.6.4
Release:	26%{?dist}
BuildArch:	noarch
Summary:	Erlang Build Tools
License:	MIT
URL:		https://github.com/%{upstream}/%{realname}
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Source1:	rebar.escript
# Fedora/EPEL-specific
Patch1:		rebar-0001-Load-templates-from-the-filesystem-first.patch
# Fedora/EPEL-specific
Patch2:		rebar-0002-Remove-bundled-mustache.patch
# The bundled getopt is necessary to do the initial bootstrap since
# erlang-getopt requires erlang-rebar to build and vice versa.
# Fedora/EPEL-specific
Patch3:		rebar-0003-Remove-bundled-getopt.patch
# Will be proposed for inclusion
Patch4:		rebar-0004-Allow-discarding-building-ports.patch
# Fedora/EPEL-specific - we're using at least R16B03
Patch5:		rebar-0005-Remove-any-traces-of-long-time-obsolete-escript-fold.patch
Patch6:		rebar-0006-remove-abnfc.patch
Patch7:		rebar-0007-Remove-support-for-gpb-compiler.patch
# Fedora/EPEL-specific - we're using at least R16B03
Patch8:		rebar-0008-Remove-pre-R15B02-workaround.patch
# Fedora/EPEL-specific - keep until we dump R16B03-1 and 17.x.y entirely
Patch9:		rebar-0009-Use-erlang-timestamp-0-explicitly.patch
# Fedora/EPEL-specific - allow vsn variable override
Patch10:	rebar-0010-Try-shell-variable-VSN-first.patch
# Fedora/EPEL-specific - allow overriding missind deps error (versions
# mismatch)
Patch11:	rebar-0011-Allow-ignoring-missing-deps.patch
Patch12:	rebar-0012-Drop-obsolete-crypto-rand_uniform-2.patch
Patch13:	rebar-0013-Remove-compat-random-modules.patch
# Fedora 33+
Patch14:	rebar-0014-erl_interface-was-removed-in-Erlang-23.patch
Patch15:	rebar-0015-Disable-two-test-suites-in-Erlang-24.patch

%if 0%{?need_bootstrap} < 1
BuildRequires:	erlang-rebar
# FIXME remove later and revisit getopt<->rebar bootstrapping
BuildRequires:	erlang-getopt
%else
BuildRequires:	erlang-asn1
BuildRequires:	erlang-common_test
BuildRequires:	erlang-compiler
BuildRequires:	erlang-crypto
BuildRequires:	erlang-dialyzer
BuildRequires:	erlang-diameter
BuildRequires:	erlang-edoc
BuildRequires:	erlang-eflame
BuildRequires:	erlang-erl_interface
BuildRequires:	erlang-erlydtl
BuildRequires:	erlang-erts
BuildRequires:	erlang-eunit
BuildRequires:	erlang-getopt
BuildRequires:	erlang-kernel
BuildRequires:	erlang-lfe
BuildRequires:	erlang-mustache
BuildRequires:	erlang-neotoma
BuildRequires:	erlang-parsetools
BuildRequires:	erlang-protobuffs
BuildRequires:	erlang-reltool
BuildRequires:	erlang-rpm-macros
BuildRequires:	erlang-sasl
BuildRequires:	erlang-snmp
BuildRequires:	erlang-stdlib
BuildRequires:	erlang-syntax_tools
BuildRequires:	erlang-tools
BuildRequires:	erlang-triq
%endif

# FIXME wip
#Requires:	erlang-abnfc
#Requires:	erlang-gpb

# This one cannot be picked up automatically
# See https://bugzilla.redhat.com/960079
Requires:	erlang-common_test
# Requires for port compiling - no direct references in Rebar's src/*.erl files
Requires:	erlang-erl_interface
# This one cannot be picked up automatically
# See https://bugzilla.redhat.com/960079
Requires:	erlang-parsetools

Requires:	erlang-rpm-macros >= 0.2.4
Provides:	%{realname} = %{version}-%{release}


%description
Erlang Build Tools.


%prep
%setup -q -n %{realname}-%{version}
%patch -P1 -p1 -b .load_templates_from_fs
%patch -P2 -p1 -b .remove_bundled_mustache
%if 0%{?need_bootstrap} < 1
%patch -P3 -p1 -b .remove_bundled_getopt
%endif
%patch -P4 -p1 -b .allow_discarding_ports
%patch -P5 -p1 -b .remove_escript_foldl_3
%patch -P6 -p1 -b .remove_abnfc
%patch -P7 -p1 -b .remove_gpb
%patch -P8 -p1 -b .remove_pre_R15B02
%patch -P9 -p1 -b .erlang_timestamp_0
%patch -P10 -p1 -b .vsn_override
%patch -P11 -p1 -b .skip_deps_checking
%patch -P12 -p1 -b .erl20
%patch -P13 -p1 -b .erl22_compat
%patch -P14 -p1 -b .erl23_compat
%if 0%{?fedora} >= 34
%patch -P15 -p1 -b .erl24
%endif


%build
%if 0%{?need_bootstrap} < 1
%{erlang_compile}
%else
./bootstrap
./rebar compile -v
%endif


%install
%{erlang_install}
# Install rebar script itself
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/rebar
# Copy the contents of priv folder
cp -a priv %{buildroot}%{_erllibdir}/%{realname}-%{version}/


%check
%if 0%{?need_bootstrap} < 1
# For using during tests
install -D -p -m 0755 %{SOURCE1} ./rebar
sed -i -e "s,-noshell -noinput,-noshell -noinput -pa .,g" ./rebar
%{rebar_eunit}
%endif


%files
%doc README.md THANKS rebar.config.sample
%license LICENSE
%{_bindir}/rebar
%{erlang_appdir}/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Peter Lemenkov <lemenkov@gmail.com> - 2.6.4-16
- Fixed NIF compilation with Erlang 23 (Fedora 33+)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 10 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.6.4-13
- Rebuild

* Sat Nov  9 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.6.4-12
- Bootstrap with new erlang-rpm-macros

* Thu Nov  7 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.6.4-11
- Bootstrap with Erlang 31+

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 14 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.6.4-8
- Fixed FTBFS with Erlang 20
- Make it noarch

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep  1 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.6.4-2
- Ver. 2.6.4 (rhbz#1350988)
- Re-enable upstream behaviour for get-deps (rhbz#999054)
- Added erlang-eflame dependency

* Thu Sep  1 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.6.4-1
- Bootstrap ver. 2.6.4 (rhbz#1350988)
- Re-enable upstream behaviour for get-deps (rhbz#999054)
- Added erlang-eflame dependency

* Tue Mar 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.6.1-10
- Fixed tests
- Fixed incompatibility with a newest erlang-mustache

* Mon Mar  7 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.6.1-9
- Allow skipping check for apps (not recommended for the end users - we'll use
  it only during rpm building so we won't introduce this functionality
  officially).

* Sun Mar  6 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.6.1-8
- Allow VSN override using shell environment variable of the same name.

* Thu Mar  3 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.6.1-7
- Re-add erlang-diameter as a BuildRequires again

* Wed Mar  2 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.6.1-6
- Disable gbp properly

* Wed Mar  2 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.6.1-5
- Fix dependency issues mentioned by automatic dependency checker

* Tue Mar  1 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.6.1-4
- Add (Build)Requires which weren't picked up automatically

* Tue Mar  1 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.6.1-3
- Use autogenerated dependency list

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 31 2015 Filip Andres <filip@andresovi.net> - 2.6.1-1
- Update to 2.6.1

* Fri Jul 03 2015 Filip Andres <filip@andresovi.net> - 2.6.0-1
- Update to 2.6.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 8 2014 Sam Kottler <skottler@fedoraproject.org> - 2.1.0-0.7
- Add bootstrap variable and necessary conditionals for building without external getopt

* Sun Sep 01 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.1.0-0.5
- Added missing runtime requirements

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 12 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.1.0-0.4
- backported fix for ErlyDTL templates compilation

* Wed Mar 06 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.1.0-0.3
- Don't bootstrap anymore - use rebar for building rebar

* Sun Mar 03 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.1.0-0.2
- Backported fix for suppress building *.so libraries everytime

* Sat Mar 02 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.1.0-0.1
- Ver. 2.1.0-pre
- Remove R12B-related patches (EL5-related)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 18 2012 Peter Lemenkov <lemenkov@gmail.com> - 2.0.0-3
- Fix templates

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 05 2012 Peter Lemenkov <lemenkov@gmail.com> - 2.0.0-1
- Ver. 2.0.0

* Tue May 22 2012 Peter Lemenkov <lemenkov@gmail.com> - 2-9.20120514git635d1a9
- Fix building in EL6 and Fedora

* Mon May 21 2012 Peter Lemenkov <lemenkov@gmail.com> - 2-8.20120514git635d1a9
- Explicitly list erlang-erl_interface as a dependency
- Fixed EPEL5 dependencies

* Sun May 20 2012 Peter Lemenkov <lemenkov@gmail.com> - 2-7.20120514git635d1a9
- Enable building on EL5 (remove erlydtl-related stuff on el5)
- Remove abnfc-related stff until we package it

* Wed May 16 2012 Peter Lemenkov <lemenkov@gmail.com> - 2-6.20120514git635d1a9
- Updated to the latest git snapshot

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-5.20101120git90058c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-4.20101120git90058c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 22 2010 Peter Lemenkov <lemenkov@gmail.com> - 2-3.20101120git90058c7
- Added missing buildrequires

* Sat Nov 20 2010 Peter Lemenkov <lemenkov@gmail.com> - 2-2.20101120git90058c7
- Removed bundled mustache and getopt
- Fixed license tag
- Removed wrong license text from package
- Simplified %%files section
- Fixed links (project was moved to GitHub)
- Changed versioning scheme (post-release)

* Sun Sep  5 2010 Peter Lemenkov <lemenkov@gmail.com> - 2-1
- Initial build

