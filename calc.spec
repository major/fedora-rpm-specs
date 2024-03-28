%define with_readline 1

# This is _required_ right now because disabling it doesn't
# seem to actually result in it properly _not_ being built.
%define with_custom_interface 1

License:       LGPL-2.1-only AND Unlicense

Name:          calc
Version:       2.15.0.6
Release:       %autorelease
Summary:       Arbitrary precision arithmetic system and calculator

# Also, https://github.com/lcn2/calc
URL:           http://isthe.com/chongo/tech/comp/calc/
Source0:       https://github.com/lcn2/calc/releases/download/v%{version}/calc-%{version}.tar.bz2

BuildRequires: gcc, sed, util-linux

# used in creating 'calc.usage'
BuildRequires: man-db

# for compatibility with the Debian package name
Provides:      apcalc

%if %{with_readline}
# If readline-devel < 5.2-3, READLINE_EXTRAS must be set to 
# "-lhistory -lncurses" or some variant (e.g. -ltinfo).
# If readline-devel < 4.2, something else goes horribly wrong.
BuildRequires: ncurses-devel >= 5.2-26, readline-devel >= 5.2-3
%endif
BuildRequires: make

Recommends:    less >= 358
Recommends:    %{name}-stdrc

%description
Calc is an arbitrary precision C-like arithmetic system that is a
calculator, an algorithm-prototyper, and a mathematical research tool. Calc
comes with a rich set of built-in mathematical and programmatic functions.


%package libs
Summary:       Libraries for the calc arithmetic system

%description libs
Shared libraries used by the calc command line calculator and other programs
using its arbitrary precision arithmetic routines.


%package devel
Summary:        Development files for the calc arithmetic system
Requires:       %{name}-libs = %{version}-%{release}

%description devel
This package contains files necessary to build applications which use the
calc arbitrary precision arithmetic system.


%package stdrc
Summary:      Standard resource files the calc arithmetic system
Requires:     %{name} = %{version}-%{release}

%description stdrc
This package contains the standard calc resource files and several calc
shell scripts. They serve as examples of the calc language and may also be
useful in themselves.


%prep
%autosetup -p1


%build

# note parallel make (-j3, or whatever) doesn't work correctly.
make DEBUG="%{optflags}" \
%if %{with_custom_interface}
     ALLOW_CUSTOM="-DCUSTOM" \
%else
     ALLOW_CUSTOM="-UCUSTOM" \
%endif
     LD_SHARE="" \
%if %{with_readline}
     USE_READLINE="-DUSE_READLINE" \
     READLINE_LIB="-lreadline" \
     READLINE_EXTRAS="" \
%else
     USE_READLINE="" \
%endif
     HAVE_FPOS="-DHAVE_NO_FPOS" \
     ARCH_CFLAGS="" \
     PREFIX=%{_prefix} \
     LIBDIR=%{_libdir} \
     Q="" V="@" \
     all


%install

make T=%{buildroot} \
%if %{with_custom_interface}
     ALLOW_CUSTOM="-DCUSTOM" \
%else
     ALLOW_CUSTOM="-UCUSTOM" \
%endif
     PREFIX=%{_prefix} \
     LIBDIR=%{_libdir} \
     SCRIPTDIR=%{_datadir}/%{name}/cscript \
     install

%if %{with_readline} 
  # only used with internal line editor
  rm -f %{buildroot}/%{_datadir}/%{name}/bindings
%endif


%if ! %{with_custom_interface}
  # if we don't enable the custom interface, don't ship symlinks to it
  rm %{buildroot}/%{_libdir}/libcustcalc.so*
  # this shouldn't be getting installed, but... is.
  chmod +w %{buildroot}/%{_datadir}/calc/custhelp/*
  chmod +w %{buildroot}/%{_datadir}/calc/custom/*
  rm %{buildroot}/%{_datadir}/calc/custhelp/*
  rm %{buildroot}/%{_datadir}/calc/custom/*
  rmdir %{buildroot}/%{_datadir}/calc/custhelp
  rmdir %{buildroot}/%{_datadir}/calc/custom/
%endif

# Changing permissions of executables to 755 to please rpmlint.
chmod 755 %{buildroot}%{_datadir}/%{name}/cscript/*
chmod 755 %{buildroot}%{_bindir}/calc

# Fix permissions of libcalc, which upstream is now shipping non-executable
# for some reason
chmod 755 %{buildroot}/%{_libdir}/libcalc.so.%{version}

# move these so the doc macro can find them
mv %{buildroot}%{_datadir}/%{name}/README README-standard-resource
mv cscript/README README-cscript


%check
make chk
     

%ldconfig_scriptlets libs


%files
%doc BUGS CHANGES README.FIRST README.md
%license COPYING-LGPL
%{_bindir}/calc
%{_mandir}/man1/calc.1*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/help
%{_datadir}/%{name}/help/*
%if %{with_custom_interface}
%dir %{_datadir}/%{name}/custhelp
%{_datadir}/%{name}/custhelp/*
%endif
%if ! %{with_readline}
%{_datadir}/%{name}/bindings
%endif

%files libs
%doc BUGS CHANGES
%license COPYING-LGPL
%{_libdir}/libcalc.so.*
%if %{with_custom_interface}
%{_libdir}/libcustcalc.so.*
%endif

%files devel
%doc LIBRARY
%{_libdir}/libcalc.so
%if %{with_custom_interface}    
%{_libdir}/libcustcalc.so
%endif
%dir %{_includedir}/calc
%{_includedir}/calc/*.h

%files stdrc
%doc README-standard-resource README-cscript
%dir %{_datadir}/%{name}/cscript
%{_datadir}/%{name}/cscript/*
%if %{with_custom_interface}
%dir %{_datadir}/%{name}/custom
%{_datadir}/%{name}/custom/*
%endif
%{_datadir}/%{name}/*.cal
%{_datadir}/%{name}/*.line


%changelog
%autochangelog
