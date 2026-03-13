# Fedora spec initially based on upstream spec file from OBS:
# https://build.opensuse.org/package/view_file/devel:openQA/os-autoinst/os-autoinst.spec
# License: GPLv2+

# Full stack test only runs reliably on these arches, and they're all
# we really care about
%ifnarch %{ix86} x86_64
%global no_fullstack 1
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
%global github_version  5
%global github_commit   72cabd06219204bb1c60c664ac5edbd87f26e030
# if set, will be a post-release snapshot build, otherwise a 'normal' build
%global github_date     20260123
%global shortcommit     %(c=%{github_commit}; echo ${c:0:7})

Name:           os-autoinst
Version:        %{github_version}%{?github_date:^%{github_date}git%{shortcommit}}
Release:        %{autorelease}
Summary:        OS-level test automation
# there are some files under other licenses in the tarball, but we
# do not distribute any of them in the binary packages
License:        GPL-2.0-or-later
URL:            https://github.com/os-autoinst/os-autoinst
ExcludeArch:    %{ix86}
Source0:        https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{github_name}-%{github_commit}.tar.gz

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
# they have iproute2, we have iproute
# The following line is generated from dependencies.yaml (upstream)
%define main_requires %main_requires_additional git-core iproute iputils jq openssh-clients perl(B::Deparse) perl(Carp) perl(Carp::Always) perl(Config) perl(Cpanel::JSON::XS) perl(Crypt::DES) perl(Cwd) perl(Data::Dumper) perl(Digest::MD5) perl(DynaLoader) perl(English) perl(Errno) perl(Exception::Class) perl(Exporter) perl(ExtUtils::testlib) perl(Fcntl) perl(Feature::Compat::Try) perl(File::Basename) perl(File::Find) perl(File::Map) perl(File::Path) perl(File::Temp) perl(File::Which) perl(File::chdir) perl(IO::Handle) perl(IO::Scalar) perl(IO::Select) perl(IO::Socket) perl(IO::Socket::INET) perl(IO::Socket::UNIX) perl(IPC::Open3) perl(IPC::Run::Debug) perl(IPC::System::Simple) perl(JSON::Validator) perl(List::MoreUtils) perl(List::Util) perl(Mojo::IOLoop::ReadWriteProcess) >= 0.26 perl(Mojo::JSON) perl(Mojo::Log) perl(Mojo::URL) perl(Mojo::UserAgent) perl(Mojolicious) >= 9.34 perl(Mojolicious::Lite) perl(Net::DBus) perl(Net::IP) perl(Net::SNMP) perl(Net::SSH2) perl(POSIX) perl(Scalar::Util) perl(Socket) perl(Socket::MsgHdr) perl(Term::ANSIColor) perl(Thread::Queue) perl(Time::HiRes) perl(Time::Moment) perl(Time::Seconds) perl(XML::LibXML) perl(XML::SemanticDiff) perl(YAML::PP) perl(YAML::XS) perl(autodie) perl(base) perl(constant) perl(integer) perl(strict) perl(version) perl(warnings) rsync sshpass
# diff from SUSE: SUSE has python3-yamllint, Fedora has just yamllint
# The following line is generated from dependencies.yaml (upstream)
%define yamllint_requires yamllint
# all requirements needed by the tests, do not require on this in the package
# itself or any sub-packages
# diff from SUSE: replaced qemu with qemu-kvm, qemu-tools with
# qemu-img, qemu-x86 with qemu-system-i386, xorg-x11-Xvnc with
# file dep on /usr/bin/Xvnc (as it's in different packages in
# different releases)
# SUSE just has 'ipxe-bootimgs', we have -aarch64 and -x86
# The following line is generated from dependencies.yaml (upstream)
%define test_base_requires %main_requires cpio icewm ipxe-bootimgs-x86 ipxe-bootimgs-aarch64 perl(Benchmark) perl(Devel::Cover) perl(FindBin) perl(Pod::Coverage) perl(Test::Mock::Time) perl(Test::MockModule) perl(Test::MockObject) perl(Test::MockRandom) perl(Test::Mojo) perl(Test::Most) perl(Test::Output) perl(Test::Pod) perl(Test::Strict) perl(Test::Warnings) >= 0.029 procps python3-setuptools qemu-kvm /usr/bin/qemu-img /usr/bin/qemu-system-i386 socat /usr/bin/Xvnc xterm xterm-console
# The following line is generated from dependencies.yaml (upstream)
%define test_version_only_requires perl(Mojo::IOLoop::ReadWriteProcess) >= 0.28
# diff from SUSE: it's python3-pillow-tk, not python3-Pillow-tk, and
# ffmpeg-free, not ffmpeg
# we don't use test_non_s390_requires because on Fedora all the deps
# are available on s390x, ditto python_support_requires
# we don't use lua_support_requires because perl-Inline-Lua isn't
# packaged on Fedora at all
# The following line is generated from dependencies.yaml (upstream)
%define test_requires %build_requires %ocr_requires %test_base_requires %yamllint_requires ffmpeg-free perl(Inline::Python) perl(YAML::PP) python3-pillow-tk
%ifnarch s390x
# The following line is generated from dependencies.yaml
%define devel_non_s390_requires ShellCheck
%else
%define devel_non_s390_requires %{nil}
%endif
# The following line is generated from dependencies.yaml (upstream)
%define devel_requires %devel_non_s390_requires %python_style_requires %test_requires ShellCheck file perl(Code::TidyAll) perl(Devel::Cover) perl(Module::CPANfile) perl(Perl::Tidy) perl(Template::Toolkit) sed

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

# exclude unnecessary author tests
rm xt/00-tidy.t tools/tidyall
# Remove test relying on a git working copy
rm xt/30-make.t
%ifarch aarch64
# https://progress.opensuse.org/issues/194359
rm -f t/28-signalblocker.t
%endif

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
# the default is 4 seconds, ppc64le is often a bit slower
export EXPECTED_ISOTOVIDEO_RUNTIME=8
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
%{_bindir}/os-autoinst-generate-needle-preview
%{_bindir}/os-autoinst-setup-multi-machine

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
%autochangelog
