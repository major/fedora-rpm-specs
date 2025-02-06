%global basever 7.3
%global micro 16
#global pre ...
%global pyversion 3.9
Name:           pypy%{pyversion}
Version:        %{basever}.%{micro}%{?pre:~%{pre}}
%global version_ %{basever}.%{micro}%{?pre}
# The Python version is included in Release to workaround debuginfo conflicts
# and make pypy versions with otherwise the same version-release always sorted
# by Python version as well.
# This potentially allows tags like Obsoletes: pypy3 < %%{version}-%%{release}.
# https://bugzilla.redhat.com/2053880
%global baserelease %{autorelease -n}
Release:        %{baserelease}.%{pyversion}%{?dist}
Summary:        Python %{pyversion} implementation with a Just-In-Time compiler

# PyPy is MIT
# Python standard library is Python
# pypy/module/unicodedata is UCD
# Bundled cffi is is MIT
# Bundled pycparser is is BSD
# Bundled pycparser.ply is BSD
# Bundled bits from cryptography are ASL 2.0 or BSD
# Bundled hpy is MIT
# LGPL and another free license we'd need to ask spot about are present in some
# java jars that we're not building with atm (in fact, we're deleting them
# before building).  If we restore those we'll have to work out the new
# licensing terms
License:        MIT and Python and UCD and BSD and (ASL 2.0 or BSD)
URL:            https://www.pypy.org/

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# High-level configuration of the build:

# libmpdec (mpdecimal package in Fedora) is tightly coupled with the
# decimal module. We keep it bundled as to avoid incompatibilities
# with the packaged version.
# The version information can be found at lib_pypy/_libmpdec/mpdecimal.h
# defined as MPD_VERSION.
# See https://foss.heptapod.net/pypy/pypy/-/issues/3024
# With PyPy 7.3.4, the decimal module is not compiled
#%%global libmpdec_version 2.4.1

# Whether to use RPM build wheels from the python-{pip,setuptools}-wheel package
# Uses upstream bundled prebuilt wheels otherwise
%bcond_without rpmwheels

# We will build a "pypy" binary.
#
# Unfortunately, the JIT support is only available on some architectures.
# We will only build with JIT support on those architectures, and build without
# it on the other archs.  The resulting binary will typically be slower than
# CPython for the latter case.
%ifarch %{ix86} x86_64 %{arm} %{power64} s390x aarch64
%bcond_without jit
%else
%bcond_with jit
%endif

# Should we build the emacs JIT-viewing mode?
%bcond_without emacs

# Easy way to turn off the selftests:
%bcond_without selftests

# We refer to this subdir of the source tree in a few places during the build:
%global goal_dir pypy/goal

%if 0%{?fedora} < 39
# REMINDER: When updating the main pypy3 version for a certain Fedora release
# make sure to update the python-classroom group in https://pagure.io/fedora-comps/
#   1. locate comps-fXX.xml.in for each affected Fedora release
#   2. inside the <id>python-classroom</id> group locate <packagereq ...>pypy3.N-devel</packagereq>
#   3. change the package name to match the new version
#   4. submit changes as a pull request and make sure somebody merges it
%bcond_without main_pypy3
%else
%bcond_with main_pypy3
%endif

%ifarch %{ix86} x86_64 %{arm}
%global _package_note_linker gold
BuildRequires:  binutils-gold
%endif

# Source and patches:
Source0: https://downloads.python.org/pypy/pypy%{pyversion}-v%{version_}-src.tar.bz2

# Supply various useful RPM macros for building python modules against pypy:
#  __pypy, pypy_sitelib, pypy_sitearch
Source2: macros.pypy3

# By default, if built at a tty, the translation process renders a Mandelbrot
# set to indicate progress.
# This obscures useful messages, and may waste CPU cycles, so suppress it, and
# merely render dots:
Patch1: 001-nevertty.patch

# Patch pypy.translator.platform so that stdout from "make" etc gets logged,
# rather than just stderr, so that the command-line invocations of the compiler
# and linker are captured:
Patch6: 006-always-log-stdout.patch

# Disable the printing of a quote from IRC on startup (these are stored in
# ROT13 form in lib_pypy/_pypy_irc_topic.py).  Some are cute, but some could
# cause confusion for end-users (and many are in-jokes within the PyPy
# community that won't make sense outside of it).  [Sorry to be a killjoy]
Patch7: 007-remove-startup-message.patch

# Glibc's libcrypt was replaced with libxcrypt in f28, crypt.h header has
# to be added to privent compilation error.
# https://fedoraproject.org/wiki/Changes/Replace_glibc_libcrypt_with_libxcrypt
Patch9: 009-add-libxcrypt-support.patch

# Instead of bundled wheels, use our RPM packaged wheels from
# /usr/share/python-wheels
# We conditionally apply this, but we use autosetup, so we use Source here
Source189: 189-use-rpm-wheels.patch

# Build-time requirements:

# pypy's can be rebuilt using pypy2, rather than with CPython 2; doing so
# halves the build time.
#
# Turn it off with this bcond, to revert back to rebuilding using CPython
# and avoid a cycle in the build-time dependency graph:
# Note, pypy3 is built with pypy2, so no dependency cycle

%bcond_without build_using_pypy2
%if %{with build_using_pypy2}
BuildRequires: pypy2
%global bootstrap_python_interp pypy2
%else
# exception to use Python 2: https://pagure.io/fesco/issue/2130
BuildRequires: python2.7
%global bootstrap_python_interp python2

%endif

BuildRequires:  gcc

BuildRequires:  libffi-devel
BuildRequires:  tcl-devel < 1:9
BuildRequires:  tk-devel < 1:9

BuildRequires:  sqlite-devel

BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  ncurses-devel
BuildRequires:  expat-devel
BuildRequires:  openssl-devel
%if 0%{?fedora} >= 41
BuildRequires:  openssl-devel-engine
%endif
BuildRequires:  gdbm-devel
BuildRequires:  xz-devel

BuildRequires:  python-rpm-macros

%ifarch %{valgrind_arches}
BuildRequires:  valgrind-devel
%endif

# For recording stats:
BuildRequires:  time
BuildRequires:  /usr/bin/free

%if %{with selftests}
# Used by the selftests, though not by the build:
BuildRequires:  gc-devel

# For use in the selftests, for imposing a per-test timeout:
BuildRequires:  perl-interpreter
%endif

BuildRequires:  /usr/bin/execstack
BuildRequires:  /usr/bin/patchelf

# For byte-compiling the JIT-viewing mode:
%if %{with emacs}
BuildRequires:  emacs
%endif

# For %%autosetup -S git
BuildRequires:  %{_bindir}/git

%if %{with rpmwheels}
BuildRequires: python-setuptools-wheel
BuildRequires: python-pip-wheel
%endif

# Metadata for the core package (the JIT build):
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%if %{with main_pypy3}
Provides: pypy3 = %{version}-%{release}
Provides: pypy3%{?_isa} = %{version}-%{release}
# This is when pypy3 package was replaced:
Obsoletes: pypy3 < 7.3.4-4
# This is when pypy3 was provided by pypy3.8:
Conflicts: pypy3 < %{version}-%{release}
Obsoletes: pypy3.7 < 7.3.9-20
%if 0%{?fedora} >= 38
Obsoletes: pypy3.8 < 7.3.11-20
%endif
%endif

# This prevents ALL subpackages built from this spec to require
# /usr/bin/pypy*. Granularity per subpackage is impossible.
# It's intended for the libs package not to drag in the interpreter, see
# https://bugzilla.redhat.com/show_bug.cgi?id=1547131
# https://bugzilla.redhat.com/show_bug.cgi?id=1862082
# All other packages require the main package explicitly.
%global __requires_exclude ^/usr/bin/pypy

%description
PyPy's implementation of Python %{pyversion}, featuring a Just-In-Time compiler
on some CPU architectures, and various optimized implementations
of the standard types (strings, dictionaries, etc.).

%if %{with jit}
This build of PyPy has JIT-compilation enabled.
%else
This build of PyPy has JIT-compilation disabled, as it is not supported on this
CPU architecture.
%endif


%package libs
Summary:  Run-time libraries used by PyPy implementations of Python %{pyversion}

# We supply an emacs mode for the JIT viewer.
# (This doesn't bring in all of emacs, just the directory structure)
%if %{with emacs}
Requires: emacs-filesystem >= %{_emacs_version}
%endif

%if %{with main_pypy3}
Provides: pypy3-libs = %{version}-%{release}
Provides: pypy3-libs%{?_isa} = %{version}-%{release}
Obsoletes: pypy3-libs < 7.3.4-4
Obsoletes: pypy3.7-libs < 7.3.9-20
%if 0%{?fedora} >= 38
Obsoletes: pypy3.8-libs < 7.3.11-20
%endif
%endif

%if %{with rpmwheels}
Requires: python-setuptools-wheel
Requires: python-pip-wheel
%else
Provides: bundled(python3dist(pip)) = 23.0.1
Provides: bundled(python3dist(setuptools)) = 58.1.0
%endif

# Provides for the bundled libmpdec
%{?libmpdec_version:
Provides: bundled(mpdecimal) = %{libmpdec_version}
Provides: bundled(libmpdec) = %{libmpdec_version}
}

# Find the version in lib_pypy/cffi-XXX.dist-info/METADATA
Provides: bundled(python3dist(cffi)) = 1.17.0

# Find the version in lib_pypy/cffi/_pycparser/__init__.py
Provides: bundled(python3dist(pycparser)) = 2.22

# Find the version in lib_pypy/cffi/_pycparser/ply/__init__.py
Provides: bundled(python3dist(ply)) = 3.9

# Find the version in lib_pypy/_cffi_ssl/cryptography/__about__.py
Provides: bundled(python3dist(cryptography)) = 2.7

# Find the version in lib_pypy/hpy-XXX.dist-info/METADATA
Provides: bundled(python3dist(hpy)) = 0.9.0

%description libs
Libraries required by the various PyPy implementations of Python %{pyversion}.


%package test
Summary:  Tests for PyPy%{pyversion}
Requires: pypy%{pyversion}%{?_isa} = %{version}-%{release}
Requires: pypy%{pyversion}-libs%{?_isa} = %{version}-%{release}

%if %{with main_pypy3}
Provides: pypy3-test = %{version}-%{release}
Provides: pypy3-test%{?_isa} = %{version}-%{release}
Obsoletes: pypy3.7-test < 7.3.9-20
%if 0%{?fedora} >= 38
Obsoletes: pypy3.8-test < 7.3.11-20
%endif
%endif

%description test
Various testing modules of PyPy%{pyversion}.
Useful when you want to run the test suite of PyPy%{pyversion}.


%package devel
Summary:  Development tools for working with PyPy%{pyversion}
Requires: pypy%{pyversion}%{?_isa} = %{version}-%{release}
Requires: pypy%{pyversion}-libs%{?_isa} = %{version}-%{release}

%if %{with main_pypy3}
Provides: pypy3-devel = %{version}-%{release}
Provides: pypy3-devel%{?_isa} = %{version}-%{release}
Obsoletes: pypy3-devel < 7.3.4-4
Obsoletes: pypy3.7-devel < 7.3.9-20
%if 0%{?fedora} >= 38
Obsoletes: pypy3.8-devel < 7.3.11-20
%endif
%endif

Supplements: tox

%description devel
Header files for building C extension modules against PyPy%{pyversion}.


%prep
%autosetup -n pypy%{pyversion}-v%{version_}-src -p1 -S git

# Temporary workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1954999
%{?!apply_patch:%define apply_patch(qp:m:) {%__apply_patch %**}}

%if %{with rpmwheels}
%apply_patch -m %(basename %{SOURCE189}) %{SOURCE189}
rm lib-python/3/ensurepip/_bundled/*.whl
%endif


# Replace /usr/local/bin/python or /usr/bin/env python shebangs with /usr/bin/python2 or pypy2:
find -name "*.py" -exec \
  sed \
    -i -r -e "s@/usr/(local/)?bin/(env )?python(2|3)?@/usr/bin/%{bootstrap_python_interp}@" \
    "{}" \
    \;

for f in rpython/translator/goal/bpnn.py ; do
   # Detect shebang lines && remove them:
   sed -e '/^#!/Q 0' -e 'Q 1' $f \
      && sed -i '1d' $f
   chmod a-x $f
done

# Replace all lib-python and lib_pypy python shebangs with pypy3 (those will be shipped with pypy3-libs)
find lib-python/3 lib_pypy -name "*.py" -exec \
  sed -r -i '1s@^#!\s*/usr/bin.*(python|pypy).*@#!/usr/bin/%{name}@' \
    "{}" \
    \;

# Not needed on Linux
rm lib-python/3/idlelib/idle.bat

%ifarch %{ix86} x86_64 %{arm}
  sed -i -r 's/\$\(LDFLAGSEXTRA\)/& -fuse-ld=gold/' ./rpython/translator/platform/posix.py
%endif

%if %{without build_using_pypy2}
  # use the pycparser from PyPy even on CPython
  ln -s lib_pypy/cffi/_pycparser pycparser
%endif

# Remove windows executable binaries
rm lib-python/3/distutils/command/*.exe

%build
# Top memory usage is about 4.5GB on arm7hf
free

BuildPyPy() {
  ExeName=$1
  Options=$2

  echo "--------------------------------------------------------------"
  echo "--------------------------------------------------------------"
  echo "--------------------------------------------------------------"
  echo "STARTING BUILD OF: $ExeName"
  echo "--------------------------------------------------------------"
  echo "--------------------------------------------------------------"
  echo "--------------------------------------------------------------"

  pushd %{goal_dir}

  # The build involves invoking a python script, passing in particular
  # arguments, environment variables, etc.
  # Some notes on those follow:

  # The generated binary embeds copies of the values of all environment
  # variables.  We need to unset "RPM_BUILD_ROOT" to avoid a fatal error from
  #  /usr/lib/rpm/check-buildroot
  # during the postprocessing of the rpmbuild, complaining about this
  # reference to the buildroot


  # By default, pypy's autogenerated C code is placed in
  #    /tmp/usession-N
  #  
  # and it appears that this stops rpm from extracting the source code to the
  # debuginfo package
  #
  # The logic in pypy-1.4/pypy/tool/udir.py indicates that it is generated in:
  #    $PYPY_USESSION_DIR/usession-$PYPY_USESSION_BASENAME-N    
  # and so we set PYPY_USESSION_DIR so that this tempdir is within the build
  # location, and set $PYPY_USESSION_BASENAME so that the tempdir is unique
  # for each invocation of BuildPyPy

  # Compilation flags for C code:
  #   pypy-1.4/pypy/translator/c/genc.py:gen_makefile
  # assembles a Makefile within
  #   THE_UDIR/testing_1/Makefile
  # calling out to platform.gen_makefile
  # For us, that's
  #   pypy-1.4/pypy/translator/platform/linux.py: class BaseLinux(BasePosix):
  # which by default has:
  #   CFLAGS = ['-O3', '-pthread', '-fomit-frame-pointer',
  #             '-Wall', '-Wno-unused']
  # plus all substrings from CFLAGS in the environment.
  # This is used to generate a value for CFLAGS that's written into the Makefile

  # How will we track garbage-collection roots in the generated code?
  #   http://pypy.readthedocs.org/en/latest/config/translation.gcrootfinder.html

  export CFLAGS=$(echo "$RPM_OPT_FLAGS")

  # The generated C code leads to many thousands of warnings of the form:
  #   warning: variable 'l_v26003' set but not used [-Wunused-but-set-variable]
  # Suppress them:
  export CFLAGS=$(echo "$CFLAGS" -Wno-unused -fPIC)

  # If we're already built the JIT-enabled "pypy", then use it for subsequent
  # builds (of other configurations):
  if test -x './pypy' ; then
    INTERP='./pypy'
  else
    # First pypy build within this rpm build?
    # Fall back to using the bootstrap python interpreter, which might be a
    # system copy of pypy from an earlier rpm, or be cpython's /usr/bin/python:
    INTERP='%{bootstrap_python_interp}'
  fi

  # Here's where we actually invoke the build:
  time \
    RPM_BUILD_ROOT= \
    PYPY_USESSION_DIR=$(pwd) \
    PYPY_USESSION_BASENAME=$ExeName \
    $INTERP ../../rpython/bin/rpython  \
    --gcrootfinder=shadowstack \
    $Options \
    targetpypystandalone \
%ifarch riscv64
    --withoutmod-_continuation \
%endif
    --platlibdir=%{_lib}

  echo "--------------------------------------------------------------"
  echo "--------------------------------------------------------------"
  echo "--------------------------------------------------------------"
  echo "FINISHED BUILDING: $ExeName"
  echo "--------------------------------------------------------------"
  echo "--------------------------------------------------------------"
  echo "--------------------------------------------------------------"

  popd
}

BuildPyPy \
  pypy3 \
%if %{with jit}
  "-Ojit" \
%else
  "-O2" \
%endif
  %{nil}

%if %{with emacs}
%{_emacs_bytecompile} rpython/jit/tool/pypytrace-mode.el
%endif


%install
%global pypylibdir %{_libdir}/pypy%{pyversion}

# First, run packaging script, it will prep the installation tree in builddir
%global installation_archive_name pypy%{pyversion}-%{version_}
%global packaging_builddir builddir
%global packaged_prefix %{packaging_builddir}/%{installation_archive_name}
# We will set an arbitrary downstream-only soname version, as it is required
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/#_downstream_so_name_versioning
%global soname_version 0.1

%{bootstrap_python_interp} pypy/tool/release/package.py --archive-name '%{installation_archive_name}' --builddir '%{packaging_builddir}' --no-embedded-dependencies

# Mangle some paths to match CPython,
# see https://mail.python.org/pipermail/pypy-dev/2022-January/016310.html and the replies there
#   1. remove the "python" executables, we still want CPython as the python command
rm %{packaged_prefix}/bin/python*
#   2. remove the "pypy" symbolic link, we still want pypy2 to be that for now
rm %{packaged_prefix}/bin/pypy
#   3. remove the "pypy3" symbolic link, if this is not the main pypy3
%{!?with_main_pypy3:rm %{packaged_prefix}/bin/pypy3}
#   4. remove the .debug executbale and library
rm %{packaged_prefix}/bin/*.debug
#   5. move libpypy3.9-c.so to lib(64) and soname version it
#      https://docs.fedoraproject.org/en-US/packaging-guidelines/#_downstream_so_name_versioning
mv %{packaged_prefix}/bin/libpypy%{pyversion}-c.so %{packaged_prefix}/%{_lib}/libpypy%{pyversion}-c.so.%{soname_version}
ln -s libpypy%{pyversion}-c.so.%{soname_version} %{packaged_prefix}/%{_lib}/libpypy%{pyversion}-c.so
patchelf --set-soname libpypy%{pyversion}-c.so.%{soname_version} %{packaged_prefix}/%{_lib}/libpypy%{pyversion}-c.so.%{soname_version}
patchelf --replace-needed libpypy%{pyversion}-c.so libpypy%{pyversion}-c.so.%{soname_version} %{packaged_prefix}/bin/pypy%{pyversion}
#   6. remove stray README
rm %{packaged_prefix}/include/README
#   7. copy the main LICENSE file to pypy's libdir, as does CPython
cp -a LICENSE %{packaged_prefix}/%{_lib}/pypy%{pyversion}
#   8. remove sources, we don't install them
#      this list was created by inspecting rpmlint output before it was added
#      sources that look like they might be tests are kept and included in the test subpackage
rm -r %{packaged_prefix}/%{_lib}/pypy%{pyversion}/_blake2/impl
rm -r %{packaged_prefix}/%{_lib}/pypy%{pyversion}/_libmpdec
rm -r %{packaged_prefix}/%{_lib}/pypy%{pyversion}/_sha3/kcp
rm -r %{packaged_prefix}/%{_lib}/pypy%{pyversion}/_cffi_ssl/_cffi_src/openssl/src
rm    %{packaged_prefix}/%{_lib}/pypy%{pyversion}/_pypy_*.c

# Create the prefix and move stuff into it
mkdir -p %{buildroot}%{_prefix}
mv %{packaged_prefix}/bin     %{buildroot}%{_bindir}
mv %{packaged_prefix}/include %{buildroot}%{_includedir}
mv %{packaged_prefix}/%{_lib} %{buildroot}%{_libdir}

# Create directories we want to own
install -d -m 0755 %{buildroot}%{pypylibdir}/site-packages/__pycache__
%if "%{_lib}" == "lib64"
# The 64-bit version needs to create "site-packages" in /usr/lib/ (for
# pure-Python modules) as well as in /usr/lib64/ (for packages with extension
# modules).
install -d -m 0755 %{buildroot}%{_prefix}/lib/pypy%{pyversion}/site-packages/__pycache__
%endif


# Remove shebang lines from .py files that aren't executable, and
# remove executability from .py files that don't have a shebang line:
find \
  %{buildroot}                                                           \
  -name "*.py"                                                           \
    \(                                                                   \
       \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \;   \
             -print -exec sed -i '1d' {} \;                              \
          \)                                                             \
       -o                                                                \
       \(                                                                \
             -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \;         \
             -exec chmod a-x {} \;                                       \
        \)                                                               \
    \)

# The generated machine code doesn't need an executable stack,  but
# one of the assembler files (gcmaptable.s) doesn't have the necessary
# metadata to inform gcc of that, and thus gcc pessimistically assumes
# that the built binary does need an executable stack.
#
# Reported upstream as: https://codespeak.net/issue/pypy-dev/issue610
#
# I tried various approaches involving fixing the build, but the simplest
# approach is to postprocess the ELF file:
execstack --clear-execstack %{buildroot}%{_bindir}/pypy%{pyversion}

# Bytecompile all of the .py files we ship, using our pypy binary, giving us
# .pyc files for pypy.
#
# Note that some of the test files deliberately contain syntax errors, so
# we are running it in subshell, to be able to ignore the failures and not to terminate the build.
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
(%{py_byte_compile %{buildroot}%{_bindir}/pypy%{pyversion} %{buildroot}}) || :

%{buildroot}%{_bindir}/pypy%{pyversion} -c 'import _tkinter'
%{buildroot}%{_bindir}/pypy%{pyversion} -c 'import tkinter'
%{buildroot}%{_bindir}/pypy%{pyversion} -c 'import _sqlite3'
%{buildroot}%{_bindir}/pypy%{pyversion} -c 'import _curses'
%{buildroot}%{_bindir}/pypy%{pyversion} -c 'import curses'
%{buildroot}%{_bindir}/pypy%{pyversion} -c 'import syslog'
%{buildroot}%{_bindir}/pypy%{pyversion} -c 'from _sqlite3 import *'

unset LD_LIBRARY_PATH

# Capture the RPython source code files from the build within the debuginfo
# package (rhbz#666975)
%global pypy_debuginfo_dir /usr/src/debug/pypy%{pyversion}-%{version_}-src
mkdir -p %{buildroot}%{pypy_debuginfo_dir}

# copy over everything:
cp -a pypy %{buildroot}%{pypy_debuginfo_dir}

# ...then delete files that aren't:
#   - *.py files
#   - the Makefile
#   - typeids.txt
#   - dynamic-symbols-*
find \
  %{buildroot}%{pypy_debuginfo_dir}  \
  \( -type f                         \
     -a                              \
     \! \( -name "*.py"              \
           -o                        \
           -name "Makefile"          \
           -o                        \
           -name "typeids.txt"       \
           -o                        \
           -name "dynamic-symbols-*" \
        \)                           \
  \)                                 \
  -delete

# Alternatively, we could simply keep everything.  This leads to a ~350MB
# debuginfo package, but it makes it easy to hack on the Makefile and C build
# flags by rebuilding/linking the sources.
# To do so, remove the above "find" command.

# We don't need bytecode for these files; they are being included for reference
# purposes.
# There are some rpmlint warnings from these files:
#   non-executable-script
#   wrong-script-interpreter
#   zero-length
#   script-without-shebang
#   dangling-symlink
# but given that the objective is to preserve a copy of the source code, those
# are acceptable.

# Install the JIT trace mode for Emacs:
%if %{with emacs}
mkdir -p %{buildroot}/%{_emacs_sitelispdir}
cp -a rpython/jit/tool/pypytrace-mode.el %{buildroot}/%{_emacs_sitelispdir}/pypy%{pyversion}trace-mode.el
cp -a rpython/jit/tool/pypytrace-mode.elc %{buildroot}/%{_emacs_sitelispdir}/pypy%{pyversion}trace-mode.elc
%endif

%if %{with main_pypy3}
# Install macros for rpm:
install -m0644 -p -D -t %{buildroot}/%{_rpmconfigdir}/macros.d %{SOURCE2}
%endif


%check

%{?libmpdec_version:
# Verify that the bundled libmpdec version python was compiled with, is the same version we have virtual
# provides for in the SPEC.
test "$(%{goal_dir}/pypy%{pyversion}-c -c 'import decimal; print(decimal.__libmpdec_version__.decode("ascii"))')" = \
     "%{libmpdec_version}"
}

topdir=$(pwd)

SkipTest() {
    TEST_NAME=$1
    sed -i -e"s|^$TEST_NAME$||g" testnames.txt
}

CheckPyPy() {
    # We'll be exercising one of the freshly-built binaries using the
    # test suite from the standard library (overridden in places by pypy's
    # modified version)
    ExeName=$1

    echo "--------------------------------------------------------------"
    echo "--------------------------------------------------------------"
    echo "--------------------------------------------------------------"
    echo "STARTING TEST OF: $ExeName"
    echo "--------------------------------------------------------------"
    echo "--------------------------------------------------------------"
    echo "--------------------------------------------------------------"

    pushd %{goal_dir}

    # I'm seeing numerous cases where tests seem to hang, or fail unpredictably
    # So we'll run each test in its own process, with a timeout

    # Use regrtest to explicitly list all tests:
    ( ./$ExeName -c \
         "from test.libregrtest.runtest import findtests; print('\n'.join(findtests()))"
    ) > testnames.txt

    # Skip some tests:
      # "audioop" doesn't exist for pypy yet:
      SkipTest test_audioop

      # The gdb CPython hooks haven't been ported to cpyext:
      SkipTest test_gdb

      # hotshot relies heavily on _hotshot, which doesn't exist:
      SkipTest test_hotshot

      # "strop" module doesn't exist for pypy yet:
      SkipTest test_strop

      # I'm seeing Koji builds hanging e.g.:
      #   http://koji.fedoraproject.org/koji/getfile?taskID=3386821&name=build.log
      # The only test that seems to have timed out in that log is
      # test_multiprocessing, so skip it for now:
      SkipTest test_multiprocessing

    echo "== Test names =="
    cat testnames.txt
    echo "================="

    echo "" > failed-tests.txt

    for TestName in $(cat testnames.txt) ; do

        echo "===================" $TestName "===================="

        # Use /usr/bin/time (rather than the shell "time" builtin) to gather
        # info on the process (time/CPU/memory).  This passes on the exit
        # status of the underlying command
        #
        # Use perl's alarm command to impose a timeout
        #   900 seconds is 15 minutes per test.
        # If a test hangs, that test should get terminated, allowing the build
        # to continue.
        #
        # Invoke pypy on test.regrtest to run the specific test suite
        # verbosely
        #
        # For now, || true, so that any failures don't halt the build:
        ( /usr/bin/time \
           perl -e 'alarm shift @ARGV; exec @ARGV' 900 \
             ./$ExeName -m test.regrtest -v $TestName ) \
        || (echo $TestName >> failed-tests.txt) \
        || true
    done

    echo "== Failed tests =="
    cat failed-tests.txt
    echo "================="

    popd

    # Doublecheck pypy's own test suite, using the built pypy binary:

    # Disabled for now:
    #   x86_64 shows various failures inside:
    #     jit/backend/x86/test
    #   followed by a segfault inside
    #     jit/backend/x86/test/test_runner.py
    #
    #   i686 shows various failures inside:
    #     jit/backend/x86/test
    #   with the x86_64 failure leading to cancellation of the i686 build

    # Here's the disabled code:
    #    pushd pypy
    #    time translator/goal/$ExeName test_all.py
    #    popd

    echo "--------------------------------------------------------------"
    echo "--------------------------------------------------------------"
    echo "--------------------------------------------------------------"
    echo "FINISHED TESTING: $ExeName"
    echo "--------------------------------------------------------------"
    echo "--------------------------------------------------------------"
    echo "--------------------------------------------------------------"
}

%if %{with selftests}
CheckPyPy pypy%{pyversion}-c
%endif # with selftests

# Because there's a bunch of binary subpackages and creating
# /usr/share/doc/pypy3-this and /usr/share/doc/pypy3-that
# is just confusing for the user.
%global _docdir_fmt %{name}

%files
%doc README.rst
%{?with_main_pypy3:%{_bindir}/pypy3}
%{_bindir}/pypy%{pyversion}


%files libs
%doc README.rst
%license %{pypylibdir}/LICENSE
%license %{pypylibdir}/_cffi_ssl/LICENSE
%license %{pypylibdir}/cffi-*.dist-info/LICENSE
%license %{pypylibdir}/cffi/_pycparser/ply/LICENSE
%license %{pypylibdir}/hpy-*.dist-info/LICENSE
%{pypylibdir}/
%if %{with rpmwheels}
%exclude %{pypylibdir}/ensurepip/_bundled
%endif
%if "%{_lib}" == "lib64"
%{_prefix}/lib/pypy%{pyversion}/
%endif
%{_libdir}/libpypy%{pyversion}-c.so.%{soname_version}

%if %{with emacs}
%{_emacs_sitelispdir}/pypy%{pyversion}trace-mode.el
%{_emacs_sitelispdir}/pypy%{pyversion}trace-mode.elc
%endif

# Keep this synced with %%files test below
%exclude %{pypylibdir}/_ctypes_test.*
%exclude %{pypylibdir}/_pypy_testcapi.*
%exclude %{pypylibdir}/_test*
%exclude %{pypylibdir}/__pycache__/_ctypes_test*
%exclude %{pypylibdir}/__pycache__/_pypy_testcapi.*
%exclude %{pypylibdir}/__pycache__/_test*
%exclude %{pypylibdir}/test/
%exclude %{pypylibdir}/*/testing/
%exclude %{pypylibdir}/*/test/
%exclude %{pypylibdir}/*/tests/
%exclude %{pypylibdir}/idlelib/idle_test/
%exclude %{pypylibdir}/testcapi_long.h

# Keep this synced with %%files devel below
%exclude %{pypylibdir}/cffi/*.h
%exclude %{pypylibdir}/hpy/devel/


%files test
# Keep this synced with %%excluded %%files in libs
%{pypylibdir}/_ctypes_test.*
%{pypylibdir}/_pypy_testcapi.*
%{pypylibdir}/_test*
%{pypylibdir}/__pycache__/_ctypes_test*
%{pypylibdir}/__pycache__/_pypy_testcapi.*
%{pypylibdir}/__pycache__/_test*
%{pypylibdir}/test/
%{pypylibdir}/*/testing/
%{pypylibdir}/*/test/
%{pypylibdir}/*/tests/
%{pypylibdir}/idlelib/idle_test/
%{pypylibdir}/testcapi_long.h


%files devel
%dir %{_includedir}/pypy%{pyversion}
%{_includedir}/pypy%{pyversion}/*.h
%{_libdir}/libpypy%{pyversion}-c.so
%if %{with main_pypy3}
%{_rpmconfigdir}/macros.d/macros.pypy3
%endif

# Keep this synced with %%excluded %%files in libs
%{pypylibdir}/cffi/*.h
%{pypylibdir}/hpy/devel/


%changelog
%autochangelog
