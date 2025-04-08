%global srcname   Stockfish

# In src/evaluate.h,
# #define EvalFileDefaultNameBig "nn-HASH.nnue"
%global nnuehash1 1c0000000000
# #define EvalFileDefaultNameSmall "nn-HASH.nnue"
%global nnuehash2 37f18f62d772

Name:            stockfish
Version:         17.1
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

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 42
ExcludeArch:    %{ix86}
%endif

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

# Conditionals based on x86_64 microarchitecture levels provide a bit of
# future-proofing and a convenient place to write explanatory comments.  Theys
# also have the benefit of improving compatibility with some downstreams;
# https://github.com/AlmaLinux/ALESCo/pull/2#issuecomment-2637811851 and the
# following discussion.
#
# As of this writing, EPELs do not yet set the RPM architecture to anything
# other than x86_64, although Fedora and/or EPEL might change this in the
# future. (For now, Fedora’s baseline *is* x86_64.)

%ifarch x86_64_v4
# Requires AVX512F and AVX512BW.
%global sfarch x86-64-avx512
%endif

# Requires PEXT, which we believe to be present in some form on all hardware
# that supports BMI2 (which is part of x86_64-v3). On some machines
# (particularly CPUs using the Zen 2 architecture) PEXT is microcode, and this
# implementation is not as fast as expected, but this is still probably a good
# compromise for x86_64-v3 overall.
%ifarch x86_64_v3
%global sfarch x86-64-bmi2
%endif
%ifarch x86_64
%if 0%{?rhel} >= 10
# x86_64-v3 baseline, even if the RPM architecture is just x86_64
%global sfarch x86-64-bmi2
%endif
%endif

%ifarch x86_64_v2
%global sfarch x86-64-sse41-popcnt
%endif
%ifarch x86_64
%if 0%{?rhel} == 9
# x86_64-v2 baseline, even if the RPM architecture is just x86_64
%global sfarch x86-64-sse41-popcnt
%endif
%endif

%if %{undefined sfarch}
%ifarch x86_64 %{?x86_64}
# Plain x86_64 (v1), or some other version not covered above.
%global sfarch x86-64
%endif
%endif

# We can remove this once Fedora 41 reaches end-of life, as that will be the
# last place 32-bit packages are built.
%ifarch i686
# Since 32-bit packages are multilib-only, we can assume x86_64 hardware and
# therefore SSE2.
%global sfarch x86-32-sse2
%endif

%ifarch ppc64le
# POWER8
%global sfarch ppc-64-vsx
%endif

%ifarch aarch64
%global sfarch armv8
%endif

%ifarch riscv64
%global sfarch riscv64
%endif

%if %{undefined sfarch}
# default to general-64, which also works for s390x
%global sfarch general-64
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
