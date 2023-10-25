%bcond_without tests

%global srcname SwiftLint
%global forgeurl https://github.com/realm/%{srcname}

# This doesn't build with gcc
%global toolchain clang

# Whether to do release or debug builds
%global config release

%global swift_version 5.8.1

# Normally we would fail the build because:
#   ERROR   0008: file '/usr/bin/swiftlint' contains the $ORIGIN runpath
#   specifier at the wrong position in
#   [/usr/libexec/swift/5.8.1/lib/swift/linux:$ORIGIN]
# but in this case rpath is necessary because of
#   swiftlint: error while loading shared libraries: libswiftGlibc.so: cannot
#   open shared object file: No such file or directory
# As this in an internal library, this is allowed by policy per
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_rpath_for_internal_libraries
# so neuter the check instead
%global __brp_check_rpaths %{nil}

Name:           swiftlint
# To update: bump this Version, then run swiftlint-get-bundled-deps.sh
Version:        0.53.0
Release:        %autorelease
Summary:        Tool to enforce Swift style and conventions

# SwiftLint itself is MIT, the bundled deps breakdown is:
# Apache-1.0: cryptoswift
# Apache-2.0: swift-argument-parser, swift-syntax
# MIT: collectionconcurrencykit, swiftytexttable, swxmlhash, yams
# MIT AND Apache-2.0: sourcekitten
License:        MIT AND Apache-1.0 AND Apache-2.0
URL:            https://realm.github.io/%{srcname}/
Source0:        %{forgeurl}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Build cache of the bundled dependencies so we can build offline
Source1:        %{srcname}-%{version}-bundled-deps.tar.gz
Source2:        %{srcname}-%{version}-bundled-provides.txt
Source3:        swiftlint-get-bundled-deps.sh

BuildRequires:  swift-lang = %{swift_version}

# Swift only supports these arches
ExclusiveArch:  x86_64 aarch64

# Generated bundled provides list
%include %{SOURCE2}

%description
SwiftLint is a tool to enforce Swift style and conventions, loosely based on
the now archived GitHub Swift Style Guide. SwiftLint enforces the style guide
rules that are generally accepted by the Swift community. These rules are well
described in popular style guides like Kodeco's Swift Style Guide.

SwiftLint hooks into Clang and SourceKit to use the AST representation of your
source files for more accurate results.

%prep
%autosetup -n %{srcname}-%{version} -b 1

# We need to patch in the fallback path to the Swift libraries or
# SourceKittenFramework will segfault
sed -i .build/checkouts/SourceKitten/Source/SourceKittenFramework/library_wrapper.swift \
  -e 's:internal let linuxDefaultLibPath = .*:internal let linuxDefaultLibPath = "%{_libexecdir}/swift/%{swift_version}/lib":'

# There's a makefile but it uses bazel under the hood, so we make our own
# build script instead to ensure the right flags are passed
echo -n 'swift build -v -c %{config} %{?_smp_build_ncpus:-j %{_smp_build_ncpus}} ' > build.sh

# Do not pass in our build flags for the time being as they break the build
# https://bugzilla.redhat.com/show_bug.cgi?id=2242022#c8
# for flag in %%build_cflags; do
#   echo -n "-Xcc ${flag} " >> build.sh
# done
# for flag in %%build_cxxflags; do
#   echo -n "-Xcxx ${flag} " >> build.sh
# done

# We only pass the build id linker flags here instead using %%build_ldflags
# because the latter leads to a build failure with:
#   /usr/bin/ld.gold: fatal error: -f/--auxiliary may not be used without -shared
# The %%_build_id_flags macro isn't defined on EPEL 9 and earlier
%if %{defined _build_id_flags}
for flag in %(echo %_build_id_flags | tr ',' ' '); do
  # These are passed directly to the linker, not to the compiler
  if [ "$flag" != '-Wl' ]; then
    echo -n "-Xlinker ${flag} " >> build.sh
  fi
done
%else
# If we're not including the build id flags do not break the build
%undefine _missing_build_ids_terminate_build
%endif

# debugedit can't handle LLVM-generated DWARF5 yet
# https://bugzilla.redhat.com/show_bug.cgi?id=2242022#c9
echo '-Xcc -gdwarf-4 -Xcxx -gdwarf-4' >> build.sh

%build
sh -x build.sh

%install
install -Dpm0755 -t %{buildroot}%{_bindir} .build/%{config}/%{name}

%if %{with tests}
%check
swift test -v

# Make sure the binary actually runs
%{buildroot}%{_bindir}/swiftlint --help
%endif

%files
%license LICENSE
%doc README.md CHANGELOG.md Rules.md
%lang(cn) %doc README_CN.md
%lang(kr) %doc README_KR.md
%{_bindir}/%{name}

%changelog
%autochangelog
