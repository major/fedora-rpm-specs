%global srcname   Stockfish

# In src/evaluate.h,
# #define EvalFileDefaultNameBig "nn-HASH.nnue"
%global nnuehash1 1111cefa1111
# #define EvalFileDefaultNameSmall "nn-HASH.nnue"
%global nnuehash2 37f18f62d772

Name:            stockfish
Version:         17
Release:         %autorelease
#Source0:        %%{url}/files/%%{name}-%%{version}-linux.zip
Source0:         https://github.com/official-%{name}/%{srcname}/archive/sf_%{version}.zip
Summary:         Powerful open source chess engine
# The entire source is GPL-3.0-or-later, except the NNUE network file (see
# https://tests.stockfishchess.org/nns), which is CC0-1.0 and can be considered
# content.
License:         GPL-3.0-or-later AND CC0-1.0
URL:             http://%{name}chess.org

# the NN files
Source1:         https://tests.stockfishchess.org/api/nn/nn-%nnuehash1.nnue
Source2:         https://tests.stockfishchess.org/api/nn/nn-%nnuehash2.nnue

# steal some documentation from ubuntu
Source10:        https://bazaar.launchpad.net/~ubuntu-branches/ubuntu/vivid/%{name}/vivid/download/head:/engineinterface.txt-20091204230329-yljoyxocuxhxg1ot-78/engine-interface.txt#/%{name}-interface.txt
Source11:        https://bazaar.launchpad.net/~ubuntu-branches/ubuntu/vivid/%{name}/vivid/download/head:/%{name}.6-20091204230329-yljoyxocuxhxg1ot-76/%{name}.6

# polyglot support
Source20:        https://raw.githubusercontent.com/mpurland/%{name}/master/polyglot.ini#/%{name}-polyglot.ini

Patch:           https://github.com/official-%{name}/%{srcname}/commit/1776448917e49b922a762d2d08c00a3f3be10205.patch#/001-fix-for-gcc-15.patch

BuildRequires:  gcc-c++
BuildRequires:  make

#Suggests:       polyglot-chess

%description
Stockfish is a free UCI chess engine derived from Glaurung 2.1. It is not a
complete chess program, but requires some UCI compatible GUI (like XBoard with
PolyGlot, eboard, Arena, Sigma Chess, Shredder, Chess Partner or Fritz) in
order to be used comfortably. Read the documentation for your GUI of choice for
information about how to use Stockfish with your GUI.


%prep
# verify the NNUE net checksums early to catch maintainer error
test %nnuehash1 = "$(sha256sum %{SOURCE1} | cut -c1-12)"
test %nnuehash2 = "$(sha256sum %{SOURCE2} | cut -c1-12)"

#%%autosetup -n%%{name}-%%{version}-linux
%autosetup -p1 -n%{srcname}-sf_%{version}

# Verify the NNUE net checksums match the defaults defined in the sources
grep -Fq '#define EvalFileDefaultNameBig "nn-%{nnuehash1}.nnue"' src/evaluate.h
grep -Fq '#define EvalFileDefaultNameSmall "nn-%{nnuehash2}.nnue"' src/evaluate.h

cp -t. -p %{SOURCE10} %{SOURCE11}
cp -tsrc -p %{SOURCE1} %{SOURCE2}

# W: wrong-file-end-of-line-encoding
sed -i 's,\r$,,' %{name}-interface.txt

# polyglot of installed binary and disable log
sed -e 's,\(EngineDir = \).*,\1%{_bindir},' \
 -e 's,\(EngineCommand = \).*,\1%{name},' \
 -e 's,\(LogFile = \).*,\1~/,' -e 's,\(LogFile = \).*,\1false,' \
 %{SOURCE20} >polyglot.ini


%build
# This is needed on EPEL9 and older. On Fedora, it happens automatically (and
# the explicit macro invocation has no further effect).
%set_build_flags

# default to general-64, which also works for s390x
%global sfarch general-64

%ifarch x86_64
%if 0%{?rhel} >= 10
# RHEL10 requires x86_64v3.
%global sfarch x86-64-bmi2
%elif 0%{?rhel} == 9
# RHEL9 requires x86_64v2.
%global sfarch x86-64-sse41-popcnt
%else
# RHEL < 9, or not RHEL (i.e., Fedora)
%global sfarch x86-64
%endif
%endif
%ifarch i686
# Since 32-bit packages are multilib-only, we can assume x86_64 hardware and
# therefore SSE2.
%global sfarch x86-32-sse2
%endif
%ifarch ppc64le
%global sfarch ppc-64
%endif
%ifarch aarch64
%global sfarch armv8
%endif
%ifarch riscv64
%global sfarch riscv64
%endif

# NOTE: The upstream Makefile adds some flags on top of the Fedora ones.
# Most of them are harmless/redundant except -O3. However, benchmarks
# (based on the duration of `stockfish bench` in koji builders) support
# the use of -O3 here:
# Architecture | i686 | x86_64 | aarch64 | ppc64le | s390x
# -O3 speedup  | 14%% |   13%% |    10%% |    31%% |   1%%
%if 0%{?el8}
%ifarch s390x
# (EPEL8 only):
#   during GIMPLE pass: vect
#   main.cpp: In function 'main':
#   main.cpp:33:5: internal compiler error: Segmentation fault
#    int main(int argc, char* argv[]) {
#        ^
# Reducing the optimization level fixes this at the cost of some performance;
# according to the benchmarks above, the impact is trivial on s390x anyway.
sed -r -i 's/-O3//' src/Makefile
%endif
%endif
%make_build -C src profile-build ARCH=%sfarch \
    EXTRACXXFLAGS="%{build_cxxflags}" \
    EXTRALDFLAGS="%{build_ldflags}"


%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 -p src/%{name} %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man6
cp -p %{name}.6 %{buildroot}%{_mandir}/man6
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
cp -p polyglot.ini %{buildroot}%{_sysconfdir}/%{name}


%check
# run bench as a sanity check
./src/%{name} bench


%files
%license Copying.txt
%doc AUTHORS %{name}-interface.txt README.md
%{_mandir}/man*/%{name}*
%{_bindir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/polyglot.ini


%changelog
%autochangelog
