%global git_commit ee3f4d841d1ba7d5b1b57544c5068822ca92b1af
%global git_short_commit %(echo %{git_commit} | cut -c -7)

Name:           transfig
Version:        3.2.9a^20250619.%{git_short_commit}
Release:        %autorelease
Epoch:          1
Summary:        Utility for converting FIG files (made by xfig) to other formats
License:        Xfig
URL:            https://sourceforge.net/projects/mcj/
#Source0:        https://downloads.sourceforge.net/mcj/fig2dev-%{version}.tar.xz
Source0:        https://sourceforge.net/code-snapshots/git/m/mc/mcj/fig2dev.git/mcj-fig2dev-%{git_commit}.zip

Requires:       ghostscript
Requires:       bc
Requires:       netpbm-progs

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libXpm-devel
BuildRequires:  ghostscript

%description
The transfig utility creates a makefile which translates FIG (created by xfig)
or PIC figures into a specified LaTeX graphics language (for example,
PostScript(TM)). Transfig is used to create TeX documents which are portable
(i.e., they can be printed in a wide variety of environments).

Install transfig if you need a utility for translating FIG or PIC figures into
certain graphics languages.

%prep
#autosetup -p1 -n fig2dev-%{version}
%autosetup -p1 -n mcj-fig2dev-%{git_commit}
autoreconf -i
# Fix the manpage not being in UTF-8
iconv -f ISO-8859-15 -t UTF-8 man/fig2dev.1.in -o fig2dev.1.in.new
touch -r man/fig2dev.1.in fig2dev.1.in.new
mv fig2dev.1.in.new man/fig2dev.1.in

%build
%configure --enable-transfig
%make_build

%install
%make_install

%files
%doc CHANGES transfig/doc/manual.pdf
%{_bindir}/transfig
%{_bindir}/fig2dev
%{_bindir}/fig2ps2tex
%{_bindir}/pic2tpic
%{_datadir}/fig2dev/i18n/*.ps
%{_mandir}/man1/*.1.gz

%changelog
%autochangelog
