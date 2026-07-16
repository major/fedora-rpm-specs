%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitelib: %global tcl_sitelib %{_datadir}/tcl%{tcl_version}}

Summary: Collection of widgets and other packages for Tk
Name: tklib
Version: 0.5
Release: %autorelease
License: TCL
Source: http://downloads.sourceforge.net/tcllib/tklib-0.5.tar.gz
Patch0: tklib-0.5-tcl9-encoding.patch
URL: http://tcllib.sourceforge.net/
BuildArch: noarch
Requires: tcl(abi) = 8.6 tk tcllib
BuildRequires:  make
BuildRequires:  tcllib
BuildRequires:  tk >= 0:8.3.1

%description
This package is intended to be a collection of Tcl packages that provide
Tk utility functions and widgets useful to a large collection of Tcl/Tk
programmers.

%prep
%autosetup -p1

# Remove some execute permission bits on files that aren't executable
# to suppress some rpmlint warnings.
chmod a-x modules/plotchart/*.tcl
chmod a-x modules/swaplist/*.tcl
chmod a-x modules/widget/*.tcl
chmod a-x modules/diagrams/*.tcl
chmod a-x modules/khim/*.tcl
chmod a-x modules/khim/*.msg

iconv --from=ISO-8859-1 --to=UTF-8 modules/ctext/ctext.man > modules/ctext/ctext.man.new
mv -f modules/ctext/ctext.man.new modules/ctext/ctext.man

%build
# Override the setting for 'libdir'.  If this isn't done then the
# platform-independent script files will get installed in an arch-specific
# directory (such as /usr/lib or /usr/lib64).
%configure --libdir=%{tcl_sitelib}
# Don't bother running 'make' because there's nothing to build.

%install
make install DESTDIR=%{buildroot}

%check
make check

%files
%doc PACKAGES README README-0.4.txt ChangeLog license.terms
%{tcl_sitelib}/tklib*
%{_mandir}/*/*

%changelog
%autochangelog
