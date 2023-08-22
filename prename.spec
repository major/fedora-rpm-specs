Name:           prename
Version:        1.14
Release:        %autorelease
Summary:        Perl script to rename multiple files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PEDERST/rename-%{version}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEDERST/rename-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/pstray/rename/master/LICENSE
# This patch renames the executable from rename to prename
Patch0:         0001-Rename-the-executable-from-rename-to-prename.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)


%description
Prename renames the file names supplied according to the rule specified as
the first argument. The argument is a Perl expression which is expected
to modify the $_ string for at least some of the file names specified.

%prep
%autosetup -p1 -n rename-%{version}
cp %{SOURCE1} .

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
