# we don't want to either provide or require anything from _docdir, per policy
# https://docs.fedoraproject.org/en-US/packaging-guidelines/AutoProvidesAndRequiresFiltering/#_arch_specific_extensions_to_scripting_languages
%global __provides_exclude_from ^%{_docdir}/.*$
%global __requires_exclude_from ^%{_docdir}/.*$

%bcond_without tests

Name:           debhelper
Version:        13.30
Release:        %autorelease
Summary:        Helper programs for debian/rules
License:        GPL-2.0-or-later
URL:            https://tracker.debian.org/pkg/debhelper
BuildArch:      noarch
# Triplet is not recognized for ppc64le, so it switches to native builds for the testsi, resulting in a failure:
# dpkg-gencontrol: warning: unknown CC system type ppc64le-redhat-linux, falling back to default (native compilation)
ExcludeArch:    ppc64le

Source0:        http://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz
Patch0:         no_layout_deb.patch

BuildRequires:  gcc
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  man-db
BuildRequires:  fakeroot
BuildRequires:  dpkg-dev >= 1.18.0
BuildRequires:  findutils
BuildRequires:  grep
BuildRequires:  make
# https://lists.debian.org/debian-devel/2021/05/msg00141.html
BuildRequires:  perl(:VERSION) >= 5.28
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-podlators
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(strict)
BuildRequires:  po4a
BuildRequires:  sed
# Run-time:
# PerlIO::gzip || gzip
BuildRequires:  gzip
# Carp not used at tests
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
# Digest::SHA not used at tests
BuildRequires:  perl(Dpkg::Arch)
# Dpkg::BuildProfiles not used at tests
# Dpkg::Changelog::Parse not used at tests
# Dpkg::Deps not used at tests
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(parent)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Optional run-time:
BuildRequires:  perl(Dpkg::BuildFlags)
BuildRequires:  perl(Dpkg::Changelog::Debian)

%if %{with tests}
# Tests:
BuildRequires:  perl(autodie)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod)
%endif

Requires:       binutils
Requires:       dh-autoreconf >= 17
Requires:       dpkg >= 1.18.0
Requires:       dpkg-dev >= 1.18.2
Requires:       dpkg-perl >= 1.17.14
# PerlIO::gzip || gzip
Requires:       gzip
Requires:       perl(Carp)
Requires:       perl(Digest::SHA)
Requires:       perl(Dpkg::Arch)
Requires:       perl(Dpkg::BuildProfiles)
Requires:       perl(Dpkg::Changelog::Parse)
Requires:       perl(Dpkg::Deps)
Requires:       perl(File::Copy)
Requires:       perl(File::Path)
Requires:       po-debconf

Suggests:       dh-make
Suggests:       perl(Dpkg::BuildFlags)
Suggests:       perl(Dpkg::Changelog::Debian)

%description
A collection of programs that can be used in a debian/rules file to automate
common tasks related to building Debian packages. Programs are included to
install various files into your package, compress files, fix file permissions,
integrate your package with the Debian menu system, debconf, doc-base, etc.
Most Debian packages use debhelper as part of their build process.

%prep
%autosetup -p1 -n work

%build
%make_build build

%install
%make_install

# Use debhelper to install (man-pages of) debhelper...
./run dh_installman -P %{buildroot} --verbose -p debhelper

%if %{with tests}
%check
make test
%endif

%files
%doc examples/ doc/
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_mandir}/*/man1/*
%{_mandir}/*/man7/*
%{_bindir}/*
%{_datadir}/%{name}
%{perl_vendorlib}/*

%changelog
%autochangelog
