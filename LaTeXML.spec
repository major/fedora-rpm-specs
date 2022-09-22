Name:           LaTeXML
Version:        0.8.6
Release:        %autorelease
Summary:        Converts TeX and LaTeX to XML/HTML/ePub/MathML

License:        Public Domain
URL:            http://dlmf.nist.gov/LaTeXML/
Source0:        http://search.cpan.org/CPAN/authors/id/B/BR/BRMILLER/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl-generators
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(charnames)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DB_File)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long) >= 2.37
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Image::Size)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Pod::Find)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(Text::Unidecode)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(URI)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML) >= 1.61
BuildRequires:  perl(XML::LibXSLT) >= 1.58
BuildRequires:  tex(tex)
BuildRequires:  tex(latex)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Getopt::Long) >= 2.37
Requires:       perl(Image::Magick)
Requires:       perl(MIME::Base64)
Requires:       perl(Pod::Parser)
Requires:       perl(XML::LibXML) >= 1.61
Requires:       perl(XML::LibXSLT) >= 1.58
Requires:       tex(tex)
Requires:       tex(latex)
Requires(post): tex(tex)
Requires(postun): tex(tex)

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Getopt::Long\\)$
%global __requires_exclude %__requires_exclude|^perl\\(XML::LibXML\\)$
%global __requires_exclude %__requires_exclude|^perl\\(XML::LibXSLT\\)$

%description
LaTeXML is a converter that transforms TeX and LaTeX into XML/HTML/ePub/MathML
and other formats.

%prep
%autosetup -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor TEXMF=%{_texmf_main} NOMKTEXLSR
make %{?_smp_mflags}

%check
make test

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
find $RPM_BUILD_ROOT -type f -name .packlist -delete

%files
%doc Changes manual.pdf README.pod
%license LICENSE
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_texmf_main}/tex/latex/latexml/*

%post
mktexlsr >/dev/null 2>&1 || :

%postun
mktexlsr >/dev/null 2>&1 || :

%changelog
%autochangelog
