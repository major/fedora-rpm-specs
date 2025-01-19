# Fedora spec initially based on upstream spec file from OBS:
# https://build.opensuse.org/package/view_file/devel:openQA/os-autoinst/os-autoinst.spec
# License: GPLv2+

# Full stack test only runs reliably on these arches, and they're all
# we really care about
%ifnarch %{ix86} x86_64
%global no_fullstack 1
%endif

# This test fails intermittently on these arches, weird bug:
# https://github.com/mudler/Mojo-IOLoop-ReadWriteProcess/issues/20
%ifarch ppc64le s390x
%global no_osutils 1
%endif

# os-autoinst has a bunch of annoyingly-badly-named private modules,
# we do not want automatic provides or requires for these
# ref https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering#Perl
# but per https://fedorahosted.org/fpc/ticket/591 , these have been
# improved, and contrary to the wiki it is safe to set them first and
# then call perl_default_filter, the values will be properly merged.
# I tried to sell upstream on naming these properly and installing
# them to the perl vendor dir, but they wouldn't bite.
# https://github.com/os-autoinst/os-autoinst/issues/387
%global __provides_exclude_from %{_prefix}/lib/os-autoinst
%global __requires_exclude perl\\((autotest|backend|basetest|bmwqemu|commands|consoles|cv|distribution|lockapi|log|mmapi|myjsonrpc|needle|ocr|osutils|signalblocker|testapi|OpenQA::Exceptions|OpenQA::Benchmark::Stopwatch|OpenQA::Qemu|OpenQA::Isotovideo|OpenQA::NamedIOSelect)
%{?perl_default_filter}

%global github_owner    os-autoinst
%global github_name     os-autoinst
%global github_version  4.6
%global github_commit   b64e21930954562826566f2b8421324dfaff3559
# if set, will be a post-release snapshot build, otherwise a 'normal' build
%global github_date     20241125
%global shortcommit     %(c=%{github_commit}; echo ${c:0:7})

Name:           os-autoinst
Version:        %{github_version}%{?github_date:^%{github_date}git%{shortcommit}}
Release:        2%{?dist}
Summary:        OS-level test automation
# there are some files under other licenses in the tarball, but we
# do not distribute any of them in the binary packages
License:        GPL-2.0-or-later
URL:            https://os-autoinst.github.io/openQA/
ExcludeArch:    %{ix86}
Source0:        https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{github_name}-%{github_commit}.tar.gz
# https://github.com/os-autoinst/os-autoinst/pull/2550
# Fix for qemu 9.1.0+
Patch:          2550.patch

# on SUSE this is conditional, for us it doesn't have to be but we
# still use a macro just to keep build_requires similar for ease of
# cross-comparison
%define opencv_require pkgconfig(opencv)
# Ditto
%define ocr_requires tesseract tesseract-langpack-eng
# Ditto
%define python_style_requires python3-black
# The following line is generated from dependencies.yaml (upstream)
%define build_base_requires %opencv_require gcc-c++ perl(Pod::Html) pkg-config pkgconfig(fftw3) pkgconfig(libpng) pkgconfig(sndfile) pkgconfig(theoraenc)
# diff from SUSE: SUSE has 'ninja', Fedora has 'ninja-build'
# The following line is generated from dependencies.yaml (upstream)
%define build_requires %build_base_requires cmake ninja-build
# this is stuff we added to requires, we put it in its own macro
# to make resyncing with upstream spec changes easier. SUSE has
# perl-base, we have perl(base)
%define main_requires_additional perl(base)
# diff from SUSE: added main_requires_additional, dropped perl-base
# which does not exist in Fedora - we have perl(base) in
# main_requires_additional and the perl(:MODULE_COMPAT) require below
# their versioning of mojolicious is different due to
# https://github.com/openSUSE/cpanspec/issues/47
# The following line is generated from dependencies.yaml (upstream)
%define main_requires %main_requires_additional git-core perl(B::Deparse) perl(Carp) perl(Carp::Always) perl(Config) perl(Cpanel::JSON::XS) perl(Crypt::DES) perl(Cwd) perl(Data::Dumper) perl(Digest::MD5) perl(DynaLoader) perl(English) perl(Errno) perl(Exception::Class) perl(Exporter) perl(ExtUtils::testlib) perl(Fcntl) perl(File::Basename) perl(File::Find) perl(File::Map) perl(File::Path) perl(File::Temp) perl(File::Which) perl(File::chdir) perl(IO::Handle) perl(IO::Scalar) perl(IO::Select) perl(IO::Socket) perl(IO::Socket::INET) perl(IO::Socket::UNIX) perl(IPC::Open3) perl(IPC::Run::Debug) perl(IPC::System::Simple) perl(JSON::Validator) perl(List::MoreUtils) perl(List::Util) perl(Mojo::IOLoop::ReadWriteProcess) >= 0.26 perl(Mojo::JSON) perl(Mojo::Log) perl(Mojo::URL) perl(Mojo::UserAgent) perl(Mojolicious) >= 9.34 perl(Mojolicious::Lite) perl(Net::DBus) perl(Net::IP) perl(Net::SNMP) perl(Net::SSH2) perl(POSIX) perl(Scalar::Util) perl(Socket) perl(Socket::MsgHdr) perl(Term::ANSIColor) perl(Thread::Queue) perl(Time::HiRes) perl(Time::Moment) perl(Time::Seconds) perl(Try::Tiny) perl(XML::LibXML) perl(XML::SemanticDiff) perl(YAML::PP) perl(YAML::XS) perl(autodie) perl(base) perl(constant) perl(integer) perl(strict) perl(version) perl(warnings) rsync sshpass
# diff from SUSE: SUSE has python3-yamllint, Fedora has just yamllint
# The following line is generated from dependencies.yaml (upstream)
%define yamllint_requires yamllint
# all requirements needed by the tests, do not require on this in the package
# itself or any sub-packages
# diff from SUSE: replaced qemu with qemu-kvm, qemu-tools with
# qemu-img, qemu-x86 with qemu-system-i386, xorg-x11-Xvnc with
# tigervnc-server-minimal (provider of /usr/bin/Xvnc)
# SUSE just has 'ipxe-bootimgs', we have -aarch64 and -x86
# The following line is generated from dependencies.yaml (upstream)
%define test_base_requires %main_requires cpio icewm ipxe-bootimgs-x86 ipxe-bootimgs-aarch64 perl(Benchmark) perl(Devel::Cover) perl(FindBin) perl(Pod::Coverage) perl(Test::Fatal) perl(Test::Mock::Time) perl(Test::MockModule) perl(Test::MockObject) perl(Test::MockRandom) perl(Test::Mojo) perl(Test::Most) perl(Test::Output) perl(Test::Pod) perl(Test::Strict) perl(Test::Warnings) >= 0.029 procps python3-setuptools qemu-kvm /usr/bin/qemu-img /usr/bin/qemu-system-i386 socat tigervnc-server-minimal xterm xterm-console
# The following line is generated from dependencies.yaml (upstream)
%define test_version_only_requires perl(Mojo::IOLoop::ReadWriteProcess) >= 0.28
# diff from SUSE: it's python3-pillow-tk, not python3-Pillow-tk, and
# ffmpeg-free, not ffmpeg
# we don't use test_non_s390_requires because on Fedora all the deps
# are available on s390x, ditto python_support_requires
# The following line is generated from dependencies.yaml (upstream)
%define test_requires %build_requires %ocr_requires %test_base_requires %yamllint_requires ffmpeg-free perl(Inline::Python) perl(YAML::PP) python3-pillow-tk
# The following line is generated from dependencies.yaml (upstream)
%define devel_requires %python_style_requires %test_requires ShellCheck file perl(Code::TidyAll) perl(Devel::Cover) perl(Module::CPANfile) perl(Perl::Tidy) perl(Template::Toolkit) sed shfmt

BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  systemd
%if 0%{?no_fullstack}
%else
BuildRequires:  perl(Mojo::File)
%endif # no_fullstack
# tinycv is a compiled public module, so we should have this
Recommends:     tesseract
Recommends:     qemu >= 4.0.0
Recommends:     qemu-kvm
Recommends:     /usr/bin/qemu-img
# For chattr, see SUSE 'qemu_requires'
Recommends:     e2fsprogs
# Optional dependency for Python test API support
Recommends:     perl(Inline::Python)
# More efficient video encoding is done automatically if ffmpeg is present
# diff from SUSE: this is just 'ffmpeg' there
Recommends:     ffmpeg-free >= 4
BuildRequires:  %test_requires %test_version_only_requires
# For unbuffered output of Perl testsuite
BuildRequires:  expect
# tests use chattr
BuildRequires:  e2fsprogs
Requires:       %main_requires
Requires(pre):  %{_bindir}/getent
Requires(pre):  %{_sbindir}/useradd
ExcludeArch:    %{arm}

%description
The OS-autoinst project aims at providing a means to run fully
automated tests. Especially to run tests of basic and low-level
operating system components such as bootloader, kernel, installer and
upgrade, which can not easily and safely be tested with other
automated testing frameworks. However, it can just as well be used to
test applications on top of a newly installed OS.

%package devel
Summary:        Development package pulling in all build+test dependencies
Requires:       %devel_requires

%description devel
Development package pulling in all build+test dependencies.

%package openvswitch
Summary:        Open vSwitch support for os-autoinst
Requires:       openvswitch
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires(post):     dbus-tools
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
BuildRequires:      systemd

%description openvswitch
This package contains Open vSwitch support for os-autoinst.

%prep
%autosetup -n %{github_name}-%{github_commit} -p1

%if 0%{?no_fullstack}
rm -f t/99-full-stack.t
%endif # no_fullstack

%if 0%{?no_osutils}
rm -f t/13-osutils.t
%endif # no_osutils

# exclude unnecessary author tests
rm xt/00-tidy.t tools/tidyall
# Remove test relying on a git working copy
rm xt/30-make.t

%build
%cmake \
    -DOS_AUTOINST_DOC_DIR:STRING="%{_docdir}/%{name}" \
    -DOS_AUTOINST_VERSION:STRING="%{github_version}" \
    -DSYSTEMD_SERVICE_DIR:STRING="%{_unitdir}" \
    -GNinja
%ninja_build -C %{__cmake_builddir}

%install
%ninja_install -C %{__cmake_builddir} install-openvswitch
# we don't really need to ship this in the package, usually the web UI
# is much better for needle editing
rm %{buildroot}%{_prefix}/lib/os-autoinst/script/crop.py*
# this is only useful on SUSE
rm %{buildroot}%{_bindir}/os-autoinst-setup-multi-machine
# we're going to %%license this
rm %{buildroot}%{_pkgdocdir}/COPYING
ls -lR %buildroot
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -and -not -name distri -exec rmdir {} \;

# we need the stale symlinks to point to git
export NO_BRP_STALE_LINK_ERROR=yes

%check
export CI=1
# account for sporadic slowness in build environments
# https://progress.opensuse.org/issues/89059
export OPENQA_TEST_TIMEOUT_SCALE_CI=20
# We don't want fatal warnings during package building
export PERL_TEST_WARNINGS_ONLY_REPORT_WARNINGS=1
# Enable verbose test output as we can not store test artifacts within package
# build environments in case of needing to investigate failures
export PROVE_ARGS="--timer -v --nocolor"
# 00-compile-check-all.t fails if this is present and Perl::Critic is
# not installed
rm tools/lib/perlcritic/Perl/Critic/Policy/*.pm
%ninja_build -C %{__cmake_builddir} check-pkg-build

%post openvswitch
%systemd_post os-autoinst-openvswitch.service
if test $1 -eq 1 ; then
  %{_bindir}/dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig 2>&1 || :
fi

%preun openvswitch
%systemd_preun os-autoinst-openvswitch.service

%postun openvswitch
%systemd_postun_with_restart os-autoinst-openvswitch.service

%files
%{_pkgdocdir}
%license COPYING
%{perl_vendorarch}/tinycv.pm
%{perl_vendorarch}/auto/tinycv
%dir %{_prefix}/lib/os-autoinst
%{_prefix}/lib/os-autoinst/videoencoder
%{_prefix}/lib/os-autoinst/basetest.pm
#
%{_prefix}/lib/os-autoinst/dmidata
#
%{_prefix}/lib/os-autoinst/bmwqemu.pm
%{_prefix}/lib/os-autoinst/commands.pm
%{_prefix}/lib/os-autoinst/distribution.pm
%{_prefix}/lib/os-autoinst/testapi.pm
%{_prefix}/lib/os-autoinst/mmapi.pm
%{_prefix}/lib/os-autoinst/myjsonrpc.pm
%{_prefix}/lib/os-autoinst/lockapi.pm
%{_prefix}/lib/os-autoinst/log.pm
%{_prefix}/lib/os-autoinst/cv.pm
%{_prefix}/lib/os-autoinst/ocr.pm
%{_prefix}/lib/os-autoinst/osutils.pm
%{_prefix}/lib/os-autoinst/signalblocker.pm
%{_prefix}/lib/os-autoinst/needle.pm
%{_prefix}/lib/os-autoinst/backend
%{_prefix}/lib/os-autoinst/OpenQA
%{_prefix}/lib/os-autoinst/consoles
%{_prefix}/lib/os-autoinst/autotest.pm
%{_prefix}/lib/os-autoinst/*.py
%dir %{_prefix}/lib/os-autoinst/script
%{_prefix}/lib/os-autoinst/script/check_qemu_oom
%{_prefix}/lib/os-autoinst/script/dewebsockify
%{_prefix}/lib/os-autoinst/script/vnctest

%dir %{_prefix}/lib/os-autoinst/schema
%{_prefix}/lib/os-autoinst/schema/Wheels-01.yaml

%{_bindir}/isotovideo
%{_bindir}/debugviewer
%{_bindir}/snd2png

%files openvswitch
%dir %{_prefix}/lib/os-autoinst/script
%{_prefix}/lib/os-autoinst/script/os-autoinst-openvswitch
%{_unitdir}/os-autoinst-openvswitch.service
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.opensuse.os_autoinst.switch.conf

%files devel

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.6^20241125gitb64e219-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 25 2024 Adam Williamson <awilliam@redhat.com> - 4.6^20241125gitb64e219-1
- Update to latest git
- Backport PR #2550 to fix for qemu 9.1.0

* Mon Jul 29 2024 Adam Williamson <awilliam@redhat.com> - 4.6^20240729gitabb9288-3
- Update to latest git

* Thu Jul 25 2024 Sérgio Basto <sergio@serjux.com> - 4.6^20240705git12ff220-3
- Rebuild for opencv 4.10.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6^20240705git12ff220-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 12 2024 Adam Williamson <awilliam@redhat.com> - 4.6^20240705git12ff220-1
- Update to latest git, drop merged patch, update license to SPDX

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 4.6^20240609gitae652c1-2
- Perl 5.40 rebuild

* Mon Jun 10 2024 Adam Williamson <awilliam@redhat.com> - 4.6^20240609gitae652c1-1
- update to latest git, drop merged patch, update ustreamer patch

* Thu Jun 06 2024 Adam Williamson <awilliam@redhat.com> - 4.6^20240604git6646558-1
- Update to latest git, resync spec

* Mon Feb 05 2024 Sérgio Basto <sergio@serjux.com> - 4.6^20231222gitd525e04-6
- Rebuild for opencv 4.9.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6^20231222gitd525e04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6^20231222gitd525e04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 09 2024 Adam Williamson <awilliam@redhat.com> - 4.6^20231222gitd525e04-3
- Backport PR #2429 to fix issue running long commands at serial console

* Wed Jan 03 2024 Adam Williamson <awilliam@redhat.com> - 4.6^20231222gitd525e04-2
- Recommend ffmpeg-free, not ffmpeg

* Tue Jan 02 2024 Adam Williamson <awilliam@redhat.com> - 4.6^20231222gitd525e04-1
- Update to latest git

* Mon Nov 27 2023 Adam Williamson <awilliam@redhat.com> - 4.6^20231124gita2deffd-1
- Update to latest git

* Wed Oct 25 2023 Adam Williamson <awilliam@redhat.com> - 4.6^20231025git64b339c-1
- Update to latest git, resync spec

* Mon Aug 07 2023 Sérgio Basto <sergio@serjux.com> - 4.6^20230527git1946eb1-4
- Rebuild for opencv 4.8.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6^20230527git1946eb1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 4.6^20230527git1946eb1-2
- Perl 5.38 rebuild

* Fri May 26 2023 Adam Williamson <awilliam@redhat.com> - 4.6^20230527git1946eb1-1
- Update to latest git, drop merged patch, sync spec

* Wed Apr 19 2023 Adam Williamson <awilliam@redhat.com> - 4.6^20230418git6802f44-1
- Update to latest git, re-enable OCR tests

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6^20221122git5a76fb8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Sérgio Basto <sergio@serjux.com> - 4.6^20221122git5a76fb8-2
- Rebuild for opencv 4.7.0

* Wed Nov 23 2022 Adam Williamson <awilliam@redhat.com> - 4.6^20221122git5a76fb8-1
- Update to latest git, drop merged patch

* Fri Sep 23 2022 Adam Williamson <awilliam@redhat.com> - 4.6^20220923git436f134-1
- Update to latest git
- Backport PR #2177 to clean up video device handling

* Tue Aug 23 2022 Adam Williamson <awilliam@redhat.com> - 4.6^20220822giteb3f483-1
- Update to latest git

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6^20220620gitd3d433b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Sérgio Basto <sergio@serjux.com> - 4.6^20220620gitd3d433b-2
- Rebuilt for opencv 4.6.0

* Mon Jun 20 2022 Adam Williamson <awilliam@redhat.com> - 4.6^20220620gitd3d433b-1
- Update to latest git, backport PR #2096 to fix s390x properly

* Fri Jun 17 2022 Adam Williamson <awilliam@redhat.com> - 4.6^20220617gitddf414b-3
- Update to latest git, drop merged/superseded patches

* Tue Jun 07 2022 Adam Williamson <awilliam@redhat.com> - 4.6^20220530git8a7a14f-2
- Backport PR #2075 to fix warnings with perl 5.36 which break tests (#2093181)

* Thu Jun 02 2022 Adam Williamson <awilliam@redhat.com> - 4.6^20220530git8a7a14f-1
- Update to latest git, resync spec
- Include Python test support

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.6^20220201gitab6013d-2
- Perl 5.36 rebuild

* Wed Feb 02 2022 Adam Williamson <awilliam@redhat.com> - 4.6^20220201gitab6013d-1
- Update to latest git, resync spec
- Switch to newer caret-based snapshot versioning scheme
- Add xterm-console dependencies and re-enable tests that use it

* Mon Jan 24 2022 Adam Williamson <awilliam@redhat.com> - 4.6-44.20220119gitfdd1a2d
- Update to latest git, resync spec
- Disable some tests that don't work without xterm-console

* Thu Nov 25 2021 Adam Williamson <awilliam@redhat.com> - 4.6-43.20211126git627473e
- Update to latest git, resync spec
- Don't build on 32-bit ARM (tests indicate it doesn't really work anyway)
- Update test exclusions

* Fri Sep 03 2021 Adam Williamson <awilliam@redhat.com> - 4.6-42.20210803gitad28b4b
- Fix qemu-img invocation with qemu 6.1.0 (specify backing file format)

* Tue Aug 03 2021 Adam Williamson <awilliam@redhat.com> - 4.6-41.20210803gitad28b4b
- Update to latest git

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-40.20210623git5361bf1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Dan Čermák <dan.cermak@cgc-instruments.com> - 4.6-39.20210623git5361bf1
- Update to latest git, resync spec

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.6-38.20210519gitf21226c
- Perl 5.34 rebuild

* Thu May 20 2021 Adam Williamson <awilliam@redhat.com> - 4.6-37.20210519gitf21226c
- Update to latest git, resync spec, drop all patches (merged upstream)

* Thu Apr 15 2021 Adam Williamson <awilliam@redhat.com> - 4.6-36.20210326git24ec8f9
- Backport fix for a bug in the dbus change from -35 (POO #91163)
- Update dbus change patch to final version so fix applies
- Backport PR #1646 to fix floppy disablement arg with qemu 6.0

* Tue Apr 13 2021 Adam Williamson <awilliam@redhat.com> - 4.6-35.20210326git24ec8f9
- Backport upstream patch to hopefully fix crashes on isotovideo exit (#1667163)
- Try and fix dbus limit overflows due to persistent dbus connection (POO #90872)

* Tue Mar 30 2021 Adam Williamson <awilliam@redhat.com> - 4.6-34.20210326git24ec8f9
- Bump to latest git, resync spec

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.6-33.20210210git496edb5
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Feb 10 2021 Adam Williamson <awilliam@redhat.com> - 4.6-32.20210210git496edb5
- Bump to latest git again (inc. correct fix for a test issue)

* Tue Feb 09 2021 Adam Williamson <awilliam@redhat.com> - 4.6-31.20210209git2e2b378
- Bump to latest git, resync spec

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-30.20201023gitf54bdea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 03 2020 Adam Williamson <awilliam@redhat.com> - 4.6-29.20201023gitf54bdea
- Bump to recent git, resync spec
- NOTE: moves from /usr/libexec/os-autoinst to /usr/lib/os-autoinst

* Thu Oct 22 2020 Nicolas Chauvet <kwizart@gmail.com> - 4.6-28.20200804gitb781299
- Rebuilt for OpenCV

* Fri Aug 28 2020 Adam Williamson <awilliam@redhat.com> - 4.6-27.20200804gitb781299
- Backport click-and-drag support by lruzicka

* Thu Aug 27 2020 Adam Williamson <awilliam@redhat.com> - 4.6-26.20200804gitb781299
- Backport fix for a test regex with recent qemu

* Wed Aug 05 2020 Adam Williamson <awilliam@redhat.com> - 4.6-25.20200804gitb781299
- Fix OS_AUTOINST_DATA_DIR definition so @INC comes out right

* Wed Aug 05 2020 Adam Williamson <awilliam@redhat.com> - 4.6-24.20200804gitb781299
- Exclude new private module Requires from latest bump (signalblocker)

* Tue Aug 04 2020 Adam Williamson <awilliam@redhat.com> - 4.6-23.20200804gitb781299
- Bump to latest git, resync spec again

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-22.20200623git5038d8c
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-21.20200623git5038d8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Adam Williamson <awilliam@redhat.com> - 4.6-20.20200623git5038d8c
- Backport (modified) PR #1468 - make local VM host IP configurable

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.6-19.20200623git5038d8c
- Perl 5.32 rebuild

* Wed Jun 24 2020 Adam Williamson <awilliam@redhat.com> - 4.6-18.20200623git5038d8c
- Bump to latest git, resync spec again

* Fri Jun 12 2020 Adam Williamson <awilliam@redhat.com> - 4.6-17.20200610gitf38e8b1
- Drop -devel dep that doesn't exist in Fedora

* Wed Jun 10 2020 Adam Williamson <awilliam@redhat.com> - 4.6-16.20200610gitf38e8b1
- Bump to latest git, resync spec again

* Mon Jun 08 2020 Adam Williamson <awilliam@redhat.com> - 4.6-15.20200608gitbcbc6c4
- Bump to latest git, resync spec with upstream

* Thu Jun 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 4.6-14.20200430git85fa4f1
- Rebuilt for OpenCV 4.3

* Mon May 25 2020 Adam Williamson <awilliam@redhat.com> - 4.6-13.20200430git85fa4f12
- Backport PR #1419 to fix build on Rawhide (opencv4)

* Thu Apr 30 2020 Adam Williamson <awilliam@redhat.com> - 4.6-12.20200430git85fa4f12
- Bump to latest git
- Resync spec with upstream, tweak dependency macro implementation

* Fri Apr 17 2020 Adam Williamson <awilliam@redhat.com> - 4.6-11.20200414git50464d4e
- Rearrange the dependencies ppisar added

* Wed Apr 15 2020 Adam Williamson <awilliam@redhat.com> - 4.6-10.20200414git50464d4e
- Bump to latest git

* Wed Apr 01 2020 Petr Pisar <ppisar@redhat.com>
- Add more Perl dependencies

* Wed Mar 11 2020 Adam Williamson <awilliam@redhat.com> - 4.6-9.20200311git4e3dec50
- Bump to latest git

* Wed Feb 05 2020 Adam Williamson <awilliam@redhat.com> - 4.6-8.20200205git63af2f4f
- Bump to latest git

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-7.20191226gitd693abe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 4.6-6.20191226gitd693abe
- Rebuild for OpenCV 4.2

* Thu Jan 02 2020 Adam Williamson <awilliam@redhat.com> - 4.6-5.20191226gitd693abe0
- Bump to latest git

* Sun Dec 29 2019 Nicolas Chauvet <kwizart@gmail.com> - 4.6-4.20191121git75fbe1d
- Rebuilt for opencv4

* Thu Nov 21 2019 Adam Williamson <awilliam@redhat.com> - 4.6-3.20191121git75fbe1d3
- Update to latest git again

* Thu Oct 31 2019 Adam Williamson <awilliam@redhat.com> - 4.6-2.20191029git447dab86
- Properly generate -devel package

* Wed Oct 30 2019 Adam Williamson <awilliam@redhat.com> - 4.6-1.20191029git447dab86
- Bump to latest upstream git snapshot (new version 4.6 declared)
- Resync spec with upstream

* Sat Oct 19 2019 Adam Williamson <awilliam@redhat.com> - 4.5-26.20190806git3391d60
- Backport 'click_lastmatch' feature from upstream git master

* Tue Oct 15 2019 Adam Williamson <awilliam@redhat.com> - 4.5-25.20190806git3391d60
- Bump to slightly newer git snapshot to build with OpenCV 4.1

* Wed Aug 21 2019 Adam Williamson <awilliam@redhat.com> - 4.5-24.20190806gitc597122
- Backport PR #1199 to improve validate_script_output result display

* Tue Aug 20 2019 Adam Williamson <awilliam@redhat.com> - 4.5-23.20190806gitc597122
- Allow PXE boot only once (-boot once=n)

* Tue Aug 13 2019 Adam Williamson <awilliam@redhat.com> - 4.5-22.20190806gitc597122
- Disable qemu-options test on 32-bit ARM (it fails on F30)

* Tue Aug 06 2019 Adam Williamson <awilliam@redhat.com> - 4.5-21.20190806gitc597122
- Update to latest git again

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-20.20190706gitc3d5e8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Adam Williamson <awilliam@redhat.com> - 4.5-19.20190706gitc3d5e8a
- Bump to latest git again, drop merged patch

* Fri Jul 05 2019 Adam Williamson <awilliam@redhat.com> - 4.5-18.20190527git43185de
- Backport #1174 to work around RHBZ #1727388 (key press order)

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.5-17.20190527git43185de
- Perl 5.30 rebuild

* Mon May 27 2019 Adam Williamson <awilliam@redhat.com> - 4.5-16.20190527git43185de
- Bump to latest git again
- Add a couple of new/missing dependencies

* Wed Mar 13 2019 Adam Williamson <awilliam@redhat.com> - 4.5-15.20190312git1080c39
- Bump to latest git again

* Wed Feb 06 2019 Adam Williamson <awilliam@redhat.com> - 4.5-14.20190206git519f2ee
- Bump to latest git again

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-13.20190114gitdfe4780
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Adam Williamson <awilliam@redhat.com> - 4.5-12.20190114gitdfe4780
- Bump to latest git again (including virtio-rng /dev/urandom change)

* Tue Jan 08 2019 Adam Williamson <awilliam@redhat.com> - 4.5-11.20190108gitcb3fa72
- Bump to latest git again

* Tue Dec 18 2018 Adam Williamson <awilliam@redhat.com> - 4.5-10.20181213git44e93d8
- Bump to latest git again, drop backported patch

* Mon Nov 19 2018 Adam Williamson <awilliam@redhat.com> - 4.5-9.20181119gitf5d9165
- Bump to latest git again
- Backport a patch related to new video timestamp feature

* Wed Nov 14 2018 Adam Williamson <awilliam@redhat.com> - 4.5-8.20181113gitdced72b
- Bump to latest git
- Resync with upstream spec
- Disable OCR test on Rawhide as Tesseract 4.0.0 sucks

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-7.20180208gitab8eeda
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.5-6.20180208gitab8eeda
- Perl 5.28 rebuild

* Fri Mar 02 2018 Adam Williamson <awilliam@redhat.com> - 4.5-5.20180208gitab8eeda
- Rebuild for opencv 3.4.1

* Thu Feb 08 2018 Adam Williamson <awilliam@redhat.com> - 4.5-4.20180208gitab8eeda
- Bump to latest git

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-3.20171222git1c7bb3f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 02 2018 Adam Williamson <awilliam@redhat.com> - 4.5-2.20171222git1c7bb3f
- Bump to latest git, with an upstream bugfix (#901)
- Rebuild for opencv soname bump (Rawhide)

* Wed Dec 20 2017 Adam Williamson <awilliam@redhat.com> - 4.5-1.20171220git25191d5
- Bump to latest git again, bump version to 4.5 (per upstream)

* Thu Aug 17 2017 Adam Williamson <awilliam@redhat.com> - 4.4-26.20170807gitcf2d051
- Bump to latest git again (wait_screen_change enhancement looks nice)

* Tue Aug 15 2017 Adam Williamson <awilliam@redhat.com> - 4.4-25.20170725git734682a
- Revert typing speed change, didn't help and we found the real bug

* Tue Aug 15 2017 Adam Williamson <awilliam@redhat.com> - 4.4-24.20170725git734682a
- Make the default typing speed slower to work around typing fails

* Mon Jul 31 2017 Adam Williamson <awilliam@redhat.com> - 4.4-23.20170725git734682a
- Bump to latest git

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 4.4-22.20170410git97928a2
- Rebuild with binutils fix for ppc64le (#1475636)

* Tue Jul 25 2017 Adam Williamson <awilliam@redhat.com> - 4.4-21.20170410git97928a2
- Recommend git to avoid error messages in logs (RHBZ #1467086)

* Thu Jul 20 2017 Adam Williamson <awilliam@redhat.com> - 4.4-20.20170410git97928a2
- Rebuild for new gdal (for new mariadb)
- Downstream patch the full-stack test to type a bit slower

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.4-19.20170410git97928a2
- Perl 5.26 rebuild
- Fixed tests to build on Perl without dot in INC

* Mon Apr 10 2017 Adam Williamson <awilliam@redhat.com> - 4.4-18.20170410git97928a2
- Bump to latest git again
- Adjust isotovideo self-reported version at build time (as did SUSE)

* Tue Mar 28 2017 Adam Williamson <awilliam@redhat.com> - 4.4-17.20170329gitd8f75d2
- Bump again to fix assert_and_click mouse repositioning (see #744)
- Disable full-stack test on non-x86 arches

* Thu Mar 02 2017 Adam Williamson <awilliam@redhat.com> - 4.4-16.20170327git201dc4e
- Update to latest git (many useful fixes)

* Tue Feb 28 2017 Adam Williamson <awilliam@redhat.com> - 4.4-15.20170126gitc29555c
- Rebuild for new opencv

* Mon Jan 30 2017 Adam Williamson <awilliam@redhat.com> - 4.4-14.20170126gitc29555c
- Update to latest git, drop merged patch

* Wed Jan 18 2017 Adam Williamson <awilliam@redhat.com> - 4.4-13.20170104git84d91e6
- Backport fix for duplicated qemu vga options (broke ARM jobs)

* Wed Jan 04 2017 Adam Williamson <awilliam@redhat.com> - 4.4-12.20170104git84d91e6
- Update to latest git, drop merged #686 patch

* Wed Jan 04 2017 Adam Williamson <awilliam@redhat.com> - 4.4-11.20170103git26171f4
- Backport #686 to fix os-autoinst on 32-bit arches, re-enable them

* Tue Jan 03 2017 Adam Williamson <awilliam@redhat.com> - 4.4-10.20170103git26171f4
- Filter out another bogus openQA provide

* Tue Jan 03 2017 Adam Williamson <awilliam@redhat.com> - 4.4-9.20170103git26171f4
- Bump to latest git again
- Add some additional test requirements
- Disable build entirely on arches broken by POO #13822 for now

* Tue Dec 13 2016 Adam Williamson <awilliam@redhat.com> - 4.4-8.20161213git3050cfa
- bump to latest git again

* Mon Nov 28 2016 Adam Williamson <awilliam@redhat.com> - 4.4-7.20161123gitdb6d2ef
- bump to latest git (inc. garretraziel's UEFI boot order patches)
- drop patches merged upstream

* Tue Oct 25 2016 Adam Williamson <awilliam@redhat.com> - 4.4-6.20161021git9672031
- bump to latest git
- backport a couple of small fixes for perl errors
- backport #625 so we can use the distro-packaged EDK2

* Mon Sep 19 2016 Adam Williamson <awilliam@redhat.com> - 4.4-5.20160915gitba7ea22
- disable a failing test on 32-bit x86

* Thu Sep 15 2016 Adam Williamson <awilliam@redhat.com> - 4.4-4.20160915gitba7ea22
- bump to git master again, drop merged patch

* Wed Sep 14 2016 Adam Williamson <awilliam@redhat.com> - 4.4-3.20160912git62f67e7
- final version of POO #13722 fix

* Wed Sep 14 2016 Adam Williamson <awilliam@redhat.com> - 4.4-2.20160912git62f67e7
- test fix for POO #13722

* Mon Sep 12 2016 Adam Williamson <awilliam@redhat.com> - 4.4-1.20160912git62f67e7
- try a new git snapshot again, let's see how it's going
- SUSE started calling this 4.4 at some point, so let's follow along

* Sun Sep 04 2016 Adam Williamson <awilliam@redhat.com> - 4.3-26.20160902git1962d68
- slightly older git snapshot, may fix issues seen in last build

* Sat Sep 03 2016 Adam Williamson <awilliam@redhat.com> - 4.3-25.20160902git0b5d885
- bump to latest git again, drop merged patches

* Wed Aug 31 2016 Adam Williamson <awilliam@redhat.com> - 4.3-24.20160826gitcd35b40
- don't sha1sum qcow assets on shutdown (slow, blocks worker process)

* Mon Aug 29 2016 Adam Williamson <awilliam@redhat.com> - 4.3-23.20160826gitcd35b40
- apply PR #571 to try and fix POO #13456 / #12680

* Fri Aug 26 2016 Adam Williamson <awilliam@redhat.com> - 4.3-22.20160826gitcd35b40
- bump to latest git (to get bug fixes, disable verbose JSON logging)

* Tue Aug 09 2016 Adam Williamson <awilliam@redhat.com> - 4.3-21.20160712gitf5bb0fe
- fix an issue with cursor reset after assert_and_click triggering overview

* Tue Jul 12 2016 Adam Williamson <awilliam@redhat.com> - 4.3-20.20160712gitf5bb0fe
- git bump again (still fixing issues related to the shutdown rewrite)

* Mon Jul 11 2016 Adam Williamson <awilliam@redhat.com> - 4.3-19.20160711git243c036
- bump to git master one more time for PR #536 (more shutdown stuff)

* Sun Jul 10 2016 Adam Williamson <awilliam@redhat.com> - 4.3-18.20160710gitc5e11ab
- bump to git master once more with merged (updated) PR #534

* Sun Jul 10 2016 Adam Williamson <awilliam@redhat.com> - 4.3-17.20160708gitcb0f4a8
- bump to current git master again to make PR apply cleanly
- backport PR #534 to fix #535 and openQA #781

* Fri Jul 08 2016 Adam Williamson <awilliam@redhat.com> - 4.3-16.20160708git7a1901d
- bump to latest git
- drop merged PR #524 patch

* Wed Jul 06 2016 Adam Williamson <awilliam@redhat.com> - 4.3-15.20160624gitfe19b00
- include the whole of PR #524 to help fix multiple interactive mode issues

* Mon Jul 04 2016 Adam Williamson <awilliam@redhat.com> - 4.3-14.20160624gitfe19b00
- fix worker crash on job cancel (#530) with a single commit from PR #524

* Tue Jun 28 2016 Adam Williamson <awilliam@redhat.com> - 4.3-13.20160624gitfe19b00
- bump to latest upstream git, drop merged patches

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.3-12.20160408gitff760a3
- Perl 5.24 rebuild

* Tue May 03 2016 Adam Williamson <awilliam@redhat.com> - 4.3-11.20160408gitff760a3
- update the upload_logs patch to the version merged upstream

* Fri Apr 29 2016 Adam Williamson <awilliam@redhat.com> - 4.3-10.20160408gitff760a3
- add an option to prevent test dying if upload_logs fails (PR #490)

* Tue Apr 26 2016 Adam Williamson <awilliam@redhat.com> - 4.3-9.20160408gitff760a3
- fix incorrect binary path in openvswitch service file (PR #487)

* Sat Apr 23 2016 Adam Williamson <awilliam@redhat.com> - 4.3-8.20160408gitff760a3
- rebuild against updated opencv

* Fri Apr 08 2016 Adam Williamson <awilliam@redhat.com> - 4.3-7.20160408gitff760a3
- bump to current git (to go along with openQA; patch load was getting huge)

* Thu Mar 31 2016 Adam Williamson <awilliam@redhat.com> - 4.3-6
- backport: allow needles to be in nested directories (jskladan)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Adam Williamson <awilliam@redhat.com> - 4.3-4
- simplify requires/provides excludes (thanks Zbigniew)

* Fri Jan 15 2016 Adam Williamson <awilliam@redhat.com> - 4.3-3
- add perl(:MODULE_COMPAT require

* Fri Jan 15 2016 Adam Williamson <awilliam@redhat.com> - 4.3-2
- exclude provides and requires from the private modules

* Thu Jan 14 2016 Adam Williamson <awilliam@redhat.com> - 4.3-1
- new release 4.3, drop patches merged upstream
- resync with upstream spec changes
- some package review cleanups
- fix 'format not a literal' errors in new snd2png (submitted upstream)

* Tue Dec 22 2015 Adam Williamson <awilliam@redhat.com> - 4.2.1-6
- changes requested in package review:
  + improve 'find and destroy' commands
  + drop tests/ directory (upstream did this too)
  + drop git dependency (seems to be ancient stuff)
  + use %%license
  + mark dbus config file as (noreplace)
  + 'Open vSwitch' not 'openvswitch' in summary/description
  + systemd snippets for openvswitch service
  + drop useless python scripts to avoid automatic python requirements

* Thu Dec 03 2015 Adam Williamson <awilliam@redhat.com> - 4.2.1-5
- fix a bug in the UEFI patch

* Thu Dec 03 2015 Adam Williamson <awilliam@redhat.com> - 4.2.1-4
- support Fedora UEFI firmware location (submitted upstream)

* Mon Nov  2 2015 Adam Williamson <awilliam@redhat.com> - 4.2.1-3
- tweak hardcoded path patch a little (upstream request)

* Sat Oct 24 2015 Adam Williamson <awilliam@redhat.com> - 4.2.1-2
- fix a hardcoded path which is incorrect on Fedora

* Thu Oct 15 2015 Adam Williamson <awilliam@redhat.com> - 4.2.1-1
- new release 4.2.1
- merge changes from upstream

* Thu Apr 23 2015 Adam Williamson <awilliam@redhat.com> - 4.1-1.20150423git24609047
- initial Fedora package, based on OBS package
