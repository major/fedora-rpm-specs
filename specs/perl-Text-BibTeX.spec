Name:           perl-Text-BibTeX
Version:        0.90
Release:        %autorelease
Summary:        Interface to read and parse BibTeX files
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND Artistic-1.0-Perl AND ANTLR-PD
URL:            https://metacpan.org/release/Text-BibTeX
Source0:        https://cpan.metacpan.org/authors/id/A/AM/AMBS/Text-BibTeX-%{version}.tar.gz
# Patch submitted upstream: https://github.com/ambs/Text-BibTeX/pull/39
Patch0:         copy-zzpre_ast-prototype-to-match-defn.patch
BuildRequires:  chrpath
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny) >= 0.06
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::AutoConf) >= 0.320
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.27
BuildRequires:  perl(ExtUtils::LibBuilder) >= 0.02
BuildRequires:  perl(ExtUtils::Mkbootstrap)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
# These don't work?  perl(Scalar::List::Utils), perl(Scalar::Util)
BuildRequires:  perl-Scalar-List-Utils >= 1.42
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  sed
Requires:       perl-Scalar-List-Utils >= 1.42

%description
The Text::BibTeX module processes BibTeX data.  It includes object-oriented
interfaces to both BibTeX database files and individual bibliographic
entries, as well as other miscellaneous functions.

%prep
%setup -q -n Text-BibTeX-%{version}
%patch 0 -p1
chmod a-x scripts/* examples/*

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
chrpath -d $RPM_BUILD_ROOT%{_bindir}/*

%check
./Build test

%files
%doc Changes examples README README.OLD scripts THANKS btool_faq.pod
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Text*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*
%{_libdir}/*.so
# no devel package needed?
# https://fedoraproject.org/wiki/Packaging:Perl#.h_files_in_module_packages
# Note also that Debian has split off "libbtparse" (and -dev)
%{_includedir}/btparse.h

%changelog
%autochangelog
