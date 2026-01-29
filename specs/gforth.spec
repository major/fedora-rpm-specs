Name:           gforth
Version:        0.7.3
Release:        %autorelease
Summary:        Fast and portable implementation of the ANS Forth language

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.gnu.org/software/gforth/
Source:         http://www.complang.tuwien.ac.at/forth/gforth/gforth-0.7.3.tar.gz
Patch:		0001-Fix-shebang.patch
# s390 build fix from Debian (http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=544827)
Patch:		0002-Try-and-fix-the-s390-build-once-again-this-time-afte.patch
Patch:		0003-another-try-to-fix-the-build-with-O2.patch
Patch:		0004-Correct-some-of-the-configure-script-s-assumptions.patch
Patch:		0005-fixed-bug-64068-reported-by-Florian-Weimer.patch
Patch:		0006-Fix-FTBFS-with-a-modern-gcc.patch
BuildRequires:  gcc-c++
BuildRequires:  libffi-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  m4
BuildRequires:  make
Requires:       emacs-filesystem
Recommends:     libtool

%description
Gforth is a fast and portable implementation of the ANS Forth
language. It works nicely with the Emacs editor, offers some nice
features such as input completion and history, backtraces, a
decompiler and a powerful locals facility, and it even has a
manual. Gforth combines traditional implementation techniques with
newer techniques for portability and performance performance: its
inner innerpreter is direct threaded with several optimizations, but
you can also use a traditional-style indirect threaded interpreter.

%define emacs_sitestart_d  %{_datadir}/emacs/site-lisp/site-start.d
%define emacs_site_lisp  %{_datadir}/emacs/site-lisp
%define gforth_datadir %{_datadir}/gforth


%prep
%autosetup -p1

iconv -f latin1 -t utf8 AUTHORS > AUTHORS.new
mv -f AUTHORS.new AUTHORS


%build
autoreconf -iv
CFLAGS="${RPM_OPT_FLAGS} `pkg-config libffi --cflags`" %configure
# %%{_smp_mflags} breaks the build
make libdir=%{_libdir}


%install
%makeinstall
cat > $RPM_BUILD_ROOT%{gforth_datadir}/site-forth/siteinit.fs <<EOF
\ If you change this file, you need to recompile gforth.fi
EOF
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
mkdir -p $RPM_BUILD_ROOT%{gforth_datadir}/emacs
cp -f gforth.el $RPM_BUILD_ROOT%{gforth_datadir}/emacs
cat > $RPM_BUILD_ROOT%{gforth_datadir}/emacs/gforth-init.el <<EOF
(autoload 'forth-mode "gforth" "Forth mode" t)
(autoload 'run-forth "gforth" "Run Forth" t)
(add-to-list 'auto-mode-alist '("\\.fs$" . forth-mode))
EOF
for i in httpd.fs filedump.fs sieve.fs
do
   chmod 0755 $RPM_BUILD_ROOT%{_datadir}/gforth/%{version}/$i
done

install -dm 755 $RPM_BUILD_ROOT%{emacs_sitestart_d}
touch $RPM_BUILD_ROOT%{emacs_sitestart_d}/gforth-init.el
install -dm 755 $RPM_BUILD_ROOT%{emacs_site_lisp}
touch $RPM_BUILD_ROOT%{emacs_site_lisp}/gforth.el

find $RPM_BUILD_ROOT -name TAGS | xargs rm -f

%triggerin -- emacs-common
if [ -d %{emacs_sitestart_d} ]; then
  ln -sf %{gforth_datadir}/emacs/gforth-init.el %{emacs_sitestart_d} || :
  ln -sf %{gforth_datadir}/emacs/gforth.el %{emacs_site_lisp} || :
fi

%triggerun -- emacs-common
if [ $2 = 0 ]; then
  rm -f %{emacs_sitestart_d}/gforth-init.el* || :
  rm -f %{emacs_site_lisp}/gforth.el* || :
fi

%files
%license COPYING COPYING.DOC
%doc README README.vmgen NEWS NEWS.vmgen AUTHORS BUGS ChangeLog
%{_bindir}/*
%{_infodir}/*
%{_datadir}/gforth
%{_libdir}/gforth
%{_includedir}/gforth
%{_mandir}/man1/*
%ghost %{_datadir}/*emacs


%changelog
%autochangelog
