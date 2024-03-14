%define plugin check_updates
%define nagiospluginsdir %{_libdir}/nagios/plugins

# No binaries in this package
%define debug_package %{nil}

Name:          nagios-plugins-check-updates
Version:       2.0.5
Release:       %autorelease
Summary:       A Nagios plugin to check if Red Hat or Fedora system is up-to-date

License:       GPLv3+
URL:           https://github.com/matteocorti/check_updates
Source:        https://github.com/matteocorti/check_updates/releases/download/v%{version}/check_updates-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl(Carp)
BuildRequires: perl(English)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(lib)
BuildRequires: perl(Module::Install)
BuildRequires: perl(Monitoring::Plugin)
BuildRequires: perl(Monitoring::Plugin::Getopt)
BuildRequires: perl(Monitoring::Plugin::Threshold)
BuildRequires: perl(POSIX)
BuildRequires: perl(Readonly)
BuildRequires: perl(strict)
BuildRequires: perl(Test::More)
BuildRequires: perl(vars)
BuildRequires: perl(warnings)

Requires:      nagios-plugins
Requires:      which
# Yum security plugin:
#   Fedora >= 19         : yum-plugin-security (is now provided by the yum package)
#   Fedora <= 18         : yum-plugin-security (yum-utils subpackage; also provides yum-security)
#   Red Hat Enterprise 6 : yum-plugin-security (yum-utils subpackage; also provides yum-security)
#   Red Hat Enterprise 5 : yum-security (yum-utils subpackage)
#   Red Hat Enterprise 8+:

%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?fedora} && 0%{?fedora} < 31)
Requires:      yum-plugin-security
%endif

Requires:      perl(Monitoring::Plugin)

%description
%{summary}.


%prep
%setup -q -n %{plugin}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor \
    INSTALLSCRIPT=%{nagiospluginsdir} \
    INSTALLVENDORSCRIPT=%{nagiospluginsdir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name "*.pod" -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
make test


%files
%license COPYING COPYRIGHT
%doc AUTHORS.md Changes NEWS README.md
%{nagiospluginsdir}/*
%{_mandir}/man1/*.1*


%changelog
%autochangelog
