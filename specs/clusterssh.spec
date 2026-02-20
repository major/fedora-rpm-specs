Name:          clusterssh
Version:       4.18_03
Release:       %autorelease
%define modname App-ClusterSSH
%define modver v%{version}
Summary:       Secure concurrent multiple server terminal control
License:       GPL-1.0-or-later OR Artistic-1.0-Perl
URL:           https://github.com/duncs/clusterssh
Source0:       https://cpan.metacpan.org/authors/id/D/DU/DUNCS/%{modname}-%{version}.tar.gz
BuildArch:     noarch
Requires:      xterm
# 2016-05-16 attempt to fix rhbz #1025913 (crash w/o fonts)
Requires:      xorg-x11-fonts-75dpi xorg-x11-fonts-100dpi
BuildRequires: fdupes
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: xterm
BuildRequires: perl(base)
BuildRequires: perl(CPAN::Changes)
BuildRequires: perl(Cwd)
BuildRequires: perl(Data::Dump)
BuildRequires: perl(English)
BuildRequires: perl(Exception::Class)
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Glob)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(File::Temp)
BuildRequires: perl(File::Which)
BuildRequires: perl(FindBin)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Getopt::Std)
BuildRequires: perl(lib)
BuildRequires: perl(Locale::Maketext)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Module::Load)
BuildRequires: perl(Net::hostent)
BuildRequires: perl(overload)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(POSIX)
BuildRequires: perl(Readonly)
BuildRequires: perl(Socket)
BuildRequires: perl(Sort::Naturally)
BuildRequires: perl(strict)
BuildRequires: perl(Sys::Hostname)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::DistManifest)
# 2015-12-28 Test::PerlTidy Not available
#BuildRequires: perl(Test::PerlTidy)
BuildRequires: perltidy
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Test::Trap)
BuildRequires: perl(Tk) >= 800.022
BuildRequires: perl(Tk::Dialog)
BuildRequires: perl(Tk::LabEntry)
BuildRequires: perl(Tk::ROText)
BuildRequires: perl(Tk::Xlib)
BuildRequires: perl(Try::Tiny)
BuildRequires: perl(vars)
BuildRequires: perl(version)
BuildRequires: perl(warnings)
BuildRequires: perl(X11::Keysyms)
BuildRequires: perl(X11::Protocol)
BuildRequires: perl(X11::Protocol::Constants)
BuildRequires: perl(X11::Protocol::Other)
BuildRequires: perl(X11::Protocol::WM)
BuildRequires: perl(XML::Simple)

%description
Control multiple terminals open on different servers to perform administration
tasks, for example multiple hosts requiring the same configuration within a 
cluster. Not limited to use with clusters, however.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0

%fdupes %buildroot
%{_fixperms} %{buildroot}
mkdir -p %{buildroot}/%{_sysconfdir}/bash_completion.d
mv  %{buildroot}/%{_bindir}/clusterssh_bash_completion.dist \
    %{buildroot}/%{_sysconfdir}/bash_completion.d/clusterssh

%files
%doc AUTHORS Changes THANKS TODO
%{_bindir}/ccon
%{_bindir}/crsh
%{_bindir}/csftp
%{_bindir}/cssh
%{_bindir}/ctel

%{_sysconfdir}/bash_completion.d
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_privlib}/*

%changelog
%autochangelog
