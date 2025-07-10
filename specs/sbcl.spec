# build with a bootstrap Common Lisp binary
%bcond_with bootstrap

%global common_lisp_controller 1

# generate/package docs
%global docs 1

# define to enable verbose build for debugging
%global sbcl_verbose 0
%global sbcl_shell /bin/bash

# SBCL name for the architecture
%ifarch %{ix86}
%global sbcl_arch x86
%endif
%ifarch x86_64
%global sbcl_arch x86-64
%endif
%ifarch aarch64
%global sbcl_arch arm64
%endif
%ifarch %{power64}
%global sbcl_arch ppc64
%endif

Name:	 sbcl
Summary: Steel Bank Common Lisp
Version: 2.5.6
Release: %autorelease

# See COPYING for a license breakdown
# FIXME: The files in src/pcl have a license similar, but not identical, to the
# Xerox license
License: LicenseRef-Fedora-Public-Domain AND LOOP AND BSD-3-Clause
URL:	 https://sbcl.sourceforge.io/
Source0: https://downloads.sourceforge.net/sourceforge/sbcl/sbcl-%{version}-source.tar.bz2

# Upstream has riscv32 and riscv64 support, but you need a Common Lisp binary
# to bootstrap with, and none seem to be available for RISC-V.  It might be
# possible to cross-compile the bootstrap SBCL from another architecture.
#
# Architectures supported by upstream that are no longer built by Fedora:
# - 32-bit ARM
# - 32-bit PowerPC
# - MIPS
# - Sparc
ExclusiveArch: %{ix86} x86_64 aarch64 %{power64}

# Pre-generated html docs
Source1: https://downloads.sourceforge.net/sourceforge/sbcl/sbcl-%{version}-documentation-html.tar.bz2

%if %{with bootstrap}
BuildRequires: clisp
%else
BuildRequires: sbcl
%endif

%if 0%{?common_lisp_controller}
BuildRequires: common-lisp-controller
Requires:      common-lisp-controller
Requires(post): common-lisp-controller
Requires(preun): common-lisp-controller
Source200: sbcl.sh
Source201: sbcl.rc
Source202: sbcl-install-clc.lisp
%endif

Patch: sbcl-0001-Do-not-modify-CFLAGS.patch
Patch: sbcl-0002-Fix-for-mock-builds-when-proc-isn-t-available.patch
Patch: sbcl-0003-Verbose-build.patch

## upstreamable patches

## upstream patches

BuildRequires: make
BuildRequires: emacs-common
BuildRequires: gcc
BuildRequires: libzstd-devel
# %%check/tests
BuildRequires: ed
BuildRequires: hostname
BuildRequires: strace
%if 0%{?docs}
# doc generation
BuildRequires: ghostscript
BuildRequires: texinfo
BuildRequires: time
%endif

%description
Steel Bank Common Lisp (SBCL) is a Open Source development environment
for Common Lisp. It includes an integrated native compiler,
interpreter, and debugger.


%prep
%autosetup -p1

# set version.lisp-expr
sed -i.rpmver -e "s|\"%{version}\"|\"%{version}-%{release}\"|" version.lisp-expr


%build
export CFLAGS='%{build_cflags}'
export LDFLAGS='%{build_ldflags}'
export CC=gcc

export SBCL_HOME=%{_prefix}/lib/sbcl
%{?sbcl_arch:export SBCL_ARCH=%{sbcl_arch}}
%{?sbcl_shell} \
./make.sh \
  --prefix=%{_prefix} \
  --with-sb-core-compression \
  %{?sbcl_bootstrap_dir:--xc-host='clisp -on-error exit'}

# docs
%if 0%{?docs}
make -C doc/manual info

# Handle pre-generated docs
tar xvjf %{SOURCE1}
cp -av %{name}-%{version}/doc/manual/* doc/manual/
%endif


%install
mkdir -p %{buildroot}{%{_bindir},%{_prefix}/lib,%{_mandir}}

unset SBCL_HOME
export INSTALL_ROOT=%{buildroot}%{_prefix}
%{?sbcl_shell} ./install.sh

%if 0%{?common_lisp_controller}
install -m744 -p -D %{SOURCE200} %{buildroot}%{_prefix}/lib/common-lisp/bin/sbcl.sh
install -m644 -p -D %{SOURCE201} %{buildroot}%{_sysconfdir}/sbcl.rc
install -m644 -p -D %{SOURCE202} %{buildroot}%{_prefix}/lib/sbcl/install-clc.lisp
# linking ok? -- Rex
cp -p %{buildroot}%{_prefix}/lib/sbcl/sbcl.core %{buildroot}%{_prefix}/lib/sbcl/sbcl-dist.core
%endif

## Unpackaged files
rm -rfv %{buildroot}%{_docdir}/sbcl
rm -fv  %{buildroot}%{_infodir}/dir
# CVS crud
find %{buildroot} -name .cvsignore -delete
# 'test-passed' files from %%check
find %{buildroot} -name 'test-passed' -delete


%check
ERROR=0
# sanity check, essential contrib modules get built/included?
CONTRIBS="sb-posix.fasl sb-bsd-sockets.fasl"
for CONTRIB in $CONTRIBS ; do
  if [ ! -f %{buildroot}%{_prefix}/lib/sbcl/contrib/$CONTRIB ]; then
    echo "WARNING: ${CONTRIB} awol!"
    ERROR=1
    echo "ulimit -a"
    ulimit -a
  fi
done
pushd tests
# verify --version output
test "$(. ./subr.sh; "$SBCL_RUNTIME" --core "$SBCL_CORE" --version --version 2>/dev/null | cut -d' ' -f2)" = "%{version}-%{release}"
# still seeing Failure: threads.impure.lisp / (DEBUGGER-NO-HANG-ON-SESSION-LOCK-IF-INTERRUPTED)
time %{?sbcl_shell} ./run-tests.sh ||:
popd
exit $ERROR

%post
%if 0%{?common_lisp_controller}
/usr/sbin/register-common-lisp-implementation sbcl > /dev/null 2>&1 ||:
%endif

%preun
if [ $1 -eq 0 ]; then
%if 0%{?common_lisp_controller}
/usr/sbin/unregister-common-lisp-implementation sbcl > /dev/null 2>&1 ||:
%endif
fi

%files
%license COPYING
%doc BUGS CREDITS NEWS PRINCIPLES README TLA TODO
%{_bindir}/sbcl
%dir %{_prefix}/lib/sbcl/
%{_prefix}/lib/sbcl/sbcl.mk
%{_prefix}/lib/sbcl/contrib/
%{_mandir}/man1/sbcl.1*
%if 0%{?docs}
%doc doc/manual/sbcl.html
%doc doc/manual/asdf.html
%{_infodir}/asdf.info*
%{_infodir}/sbcl.info*
%endif
%if 0%{?common_lisp_controller}
%{_prefix}/lib/common-lisp/bin/*
%{_prefix}/lib/sbcl/install-clc.lisp
%{_prefix}/lib/sbcl/sbcl-dist.core
%verify(not md5 size) %{_prefix}/lib/sbcl/sbcl.core
%config(noreplace) %{_sysconfdir}/sbcl.rc
%else
%{_prefix}/lib/sbcl/sbcl.core
%endif


%changelog
%autochangelog
