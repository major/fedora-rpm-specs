# Regarding JPEG2000 support, upstream writes[1]:
#
# “You can compile dcm2niix to convert DICOM images compressed with the
# JPEG2000 transfer syntaxes 1.2.840.10008.1.2.4.90 and 1.2.840.10008.1.2.4.91.
# This is optional, as JPEG2000 is very rare in DICOMs (usually only created by
# the proprietary DCMJP2K or OsiriX). Due to the challenges discussed below
# this is a poor choice for archiving DICOM data. Rather than support
# conversion with dcm2niix, a better solution would be to use DCMJP2K to do a
# DICOM-to-DICOM conversion to a more widely supported transfer syntax.
# Unfortunately, JPEG2000 saw poor adoption as a general image format. This
# situation is unlikely to change, as JPEG2000 only offered incremental
# benefits over the simpler classic JPEG, and is outperformed by the more
# recent HEIF. This has implications for DICOM, as there is little active
# development on libraries to decode JPEG2000.  Indeed, the two popular
# open-source libraries that decode JPEG2000 have serious limitations for
# processing these images. Some JPEG2000 DICOM images can not be decoded by the
# default compilation of OpenJPEG library after version 2.1.0. On the other
# hand, the Jasper library does not handle lossy 16-bit images with good
# precision.
#
# “You can build dcm2niix with JPEG2000 decompression support using OpenJPEG
# 2.1.0. You will need to have the OpenJPEG library installed (use the package
# manager of your Linux distribution, Homebrew for macOS, or see here if you
# want to build it yourself). If you want to use a more recent version of
# OpenJPEG, it must be custom-compiled with -DOPJ_DISABLE_TPSOT_FIX compiler
# flag. I suggest building static libraries […]”
#
# Zero or one (but not both) of the following bconds may be enabled.
#
# Use OpenJPEG for JPEG2000 support?
%bcond openjpeg 1
# Use Jasper for JPEG2000 support?
# (This does not compile, so we had better not.)
%bcond jasper 0
# Remember to update License/SourceLicense as needed if changing these:
# Enable JPEG-LS support? If this is disabled, CharLS is not bundled.
%bcond jpegls 1
# Enable JNIFTI support? If this is disabled, cJSON is not bundled.
%bcond jnifti 1

Name:           dcm2niix
Version:        1.0.20250506
Release:        %autorelease
Summary:        DICOM to NIfTI converter

# The entire source is BSD-3-Clause, except:
#
# - bundled niftilib (nifti.h, nifti1_io.h/nifti1_io_core.cpp) is
#   LicenseRef-Fedora-Public-Domain
#   (https://gitlab.com/fedora/legal/fedora-license-data/-/issues/667)
# - bundled nanojpeg/ujpeg (ujpeg.h/ujpeg.cpp) is MIT (text in file headers);
#   it is removed in %%prep
# - bundled miniz (miniz.c) is Unlicense; it is removed in %%prep and does not
#   contribute to the binary RPMs
# - bundled cJSON (cJSON.h/cJSON.cpp) is MIT
# - bundled tinydir (tinydir.h) is BSD-2-Clause; it is unbundled in %%prep, but
#   the system library is still header-only, so its license still contributes to
#   the license of the binary RPM
# - bundled ucm (ucm.cmake), https://github.com/onqtam/ucm, is MIT; as a
#   build-system file, it does not contribute to the licenses of the binary RPMs
# - The JavaScript library in js/ claims to be BSD-2-Clause in package.json,
#   but it has no separate license text; in any case, it is removed in %%prep.
#   See “JavaScript library claims to be BSD-2-Clause but has no license text,”
#   https://github.com/rordenlab/dcm2niix/issues/951; the resolution was
#   “Noted, this tool uses the 2-clause license and the development branch has
#   been changed to reflect this.” We can therefore expect that the main
#   license of dcm2niix will change in the next release. For this release, we
#   retain BSD-3-Clause since that is what is in the source archive.
# - the files docs/source/dcm2niibatch.rst and docs/source/dcm2niix.rst, and
#   therefore the man pages dcm2niibatch.1 and dcm2niix.1 derived from them,
#   are FSFAP
#
# The bundled CharLS (console/charls/) is also BSD-3-Clause.
#
# Upstream was asked about bundled/vendored dependencies in accordance with
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#bundling in
#
#   Use openjpeg instead of nanojpeg if found
#   https://github.com/rordenlab/dcm2niix/issues/8
#
# and
#
#   Path to supporting external/system copies of bundled dependencies (cJSON,
#   CharLS)?
#   https://github.com/rordenlab/dcm2niix/issues/953
#
# See also the notes above virtual Provides for bundled dependencies.
License:        %{shrink:
                BSD-3-Clause AND
                BSD-2-Clause AND
                FSFAP AND
                LicenseRef-Fedora-Public-Domain AND
                MIT
                }
SourceLicense:  %{license} AND Unlicense
URL:            https://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage
%global forgeurl https://github.com/rordenlab/dcm2niix
Source:         %{forgeurl}/archive/v%{version}/dcm2niix-%{version}.tar.gz

# Update scikit-build-core to 0.11, without pyproject extra
# https://github.com/rordenlab/dcm2niix/pull/950
Patch:          %{forgeurl}/pull/950.patch
# Only compile nanojpeg/ujpeg when TurboJPEG is disabled
# https://github.com/rordenlab/dcm2niix/pull/952
Patch:          %{forgeurl}/pull/952.patch

BuildRequires:  python3-devel
BuildRequires:  gcc-c++
BuildRequires:  cmake
# Git is required for Superbuild (SuperBuild/SuperBuild.cmake)
BuildRequires:  git-core
# For man pages:
BuildRequires:  /usr/bin/sphinx-build

BuildRequires:  symlinks

%if %{with jasper}
# The dependency is written this way, but our jasper-devel does not install
# CMake files.
#BuildRequires:  cmake(Jasper)
BuildRequires:  pkgconfig(jasper)
%endif
BuildRequires:  pkgconfig(libturbojpeg)
%if %{with openjpeg}
BuildRequires:  cmake(OpenJPEG)
%endif
# Header-only, unbundled downstream
BuildRequires:  tinydir-static
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  cmake(zlib)

%if %{with jpegls}
# console/charls/
#
# Based on the statement “The included code was downloaded from the CharLS
# website on 6 June 2018” in console/charls/README.md and the dates of releases
# at https://github.com/team-charls/charls/releases, the version is no later
# than 2.0.0. Based on the presence of src/jpegstreamreader.cpp, the version is
# no earlier than 2.0.0.
#
# See: https://github.com/rordenlab/dcm2niix/issues/953#issuecomment-3017005593
# “Given that JPEG-LS is a rarely used transfer syntax,with HTJ2K supplanting
# the rationale for it, and the fact we’ve had no user-reported issues over the
# years, I would be hesitant to replace a stable, internally validated library
# with a newer system dependency that may introduce subtle incompatibilities.
# Due to the immense variability of DICOM in the wild and the limited resources
# of our team, bundling proven libraries remains the most robust and
# maintainable approach for us.”
Provides:       bundled(CharLS) = 2.0.0
%endif
# console/nifti1.h, console/nifti1_io_core.cpp
#
# This appears to be derived from something around version 1.0.0, but it has
# been forked. Upstream was asked about a path to using a system copy in
# https://github.com/rordenlab/dcm2niix/issues/8 and declined in
# https://github.com/rordenlab/dcm2niix/issues/8#issuecomment-267078678.
Provides:       bundled(niftilib) = 1.0.0
%if %{with jnifti}
# console/cJSON.{h,cpp}
#
# Version from CJSON_VERSION_{MAJOR,MINOR_PATH} in cJSON.h
#
# See: https://github.com/rordenlab/dcm2niix/issues/953#issuecomment-3017005593
# “I fully appreciate the Fedora community’s preference for system-packaged
# dependencies. However, I would encourage the deployment of the current
# version using the existing proven dependencies unless a maintainer is willing
# to devote considerable time to validation.”
# “With regards to the cJSON you can always build with it off, at least until
# this promising format gains traction.”
Provides:       bundled(cJSON) = 1.7.12
%endif
# console/base64.{h,cpp}
#
# This is copied originally from FreeBSD, e.g.
# https://web.mit.edu/freebsd/head/contrib/wpa/src/utils/base64.c, where it
# appears to belong to hostapd; it is also in the Linux version of hostapd,
# https://w1.fi/cgit/hostap/tree/src/utils/base64.c. Although the copyright
# dates carry hints, it is not straightforward to infer what version of hostapd
# this code might have been copied from.
#
# It’s unlikely that this can ever be unbundled, because the implementation is
# not distributed as a separate library or exposed for public use.
Provides:       bundled(hostapd)

%description
dcm2niix is designed to convert neuroimaging data from the DICOM format to the
NIfTI format.


%package -n python3-dcm2niix
Summary:        Thin wrapper around dcm2niix binary
# This subpackage is pure-Python and does not contain anything derived from any
# of the bundled libraries or the man pages, so only the “main” license
# applies.
License:        BSD-3-Clause

BuildArch:      noarch

Requires:       dcm2niix = %{version}-%{release}

%description -n python3-dcm2niix
%{summary}.


%prep
%autosetup -p1

# Prove we do not use the bundled miniz.
rm console/miniz.c
# Prove we do not use the bundled nanojpeg/ujpeg.
rm console/ujpeg.*
%if %{without jpegls}
# Prove we do not use the bundled CharLS.
rm -rv console/charls
%endif
%if %{without jnifti}
# Prove we do not use the bundled cJSON.
rm console/cJSON.*
%endif
# Unbundle tinydir
rm console/tinydir.h
# Prove we do not install the JavaScript library
rm -rv js

# Licenses for bundled dependencies, where practical
%if %{with jpegls}
cp -p console/charls/License.txt license-charls.txt
%endif
%if %{with jnifti}
awk '/^\/\*$/ { x=1; next }; /^\*\/$/ { exit }; x' console/cJSON.cpp |
  tee license-cjson.txt
%endif


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
# https://scikit-build-core.readthedocs.io/en/latest/configuration.html
# USE_TURBOJPEG: Use TurboJPEG to decode classic JPEG
# USE_JASPER: Build with JPEG2000 support using Jasper
# USE_OPENJPEG: Build with JPEG2000 support using OpenJPEG
# USE_JPEGLS: Build with JPEG-LS support using CharLS
# USE_JNIFTI: USE_JNIFTI
# BATCH_VERSION: Build dcm2niibatch for multiple conversions
# BUILD_DCM2NIIXFSLIB: Build libdcm2niixfs.a
#   - Avoid static libraries:
#     https://docs.fedoraproject.org/en-US/packaging-guidelines/#packaging-static-libraries
# INSTALL_DEPENDENCIES: Optionally install built dependent libraries (OpenJPEG
#                        and yaml-cpp) for future use
#   - We certainly do not want to install copies of any bundled dependencies!
# BUILD_DOCS: Build documentation (manpages)
%{pyproject_wheel \
    -Ccmake.define.USE_STATIC_RUNTIME:BOOL=OFF \
    -Ccmake.define.USE_TURBOJPEG:BOOL=ON \
    -Ccmake.define.USE_JASPER:BOOL=%{?with_jasper:ON}%{?!with_jasper:OFF} \
    -Ccmake.define.USE_OPENJPEG:STRING=%{?with_openjpeg:System}%{?!with_openjpeg:OFF} \
    -Ccmake.define.USE_JPEGLS:BOOL=%{?with_jpegls:ON}%{?!with_jpegls:OFF} \
    -Ccmake.define.USE_JNIFTI:BOOL=%{?with_jnifti:ON}%{?!with_jnifti:OFF} \
    -Ccmake.define.BATCH_VERSION:BOOL=ON \
    -Ccmake.define.BUILD_DCM2NIIXFSLIB:BOOL=OFF \
    -Ccmake.define.BUILD_DOCS:BOOL=ON \
    -Ccmake.define.YAML-CPP_IMPLEMENTATION:STRING=System \
    -Ccmake.define.ZLIB_IMPLEMENTATION:STRING=System \
    -Clogging.level=INFO \
    -Ccmake.verbose=true \
    -Ccmake.build-type="RelWithDebInfo"}


%install
%pyproject_install
%pyproject_save_files -L dcm2niix

# Clean up after the wheel installation, which has everything we need, but much
# of it far from the places we need it.
install -d '%{buildroot}%{_bindir}' '%{buildroot}%{_mandir}/man1'
for cmd in dcm2niix dcm2niibatch
do
  # The installation has treated %%{python3_sitearch} like the prefix.
  mv "%{buildroot}%{python3_sitearch}/bin/${cmd}" '%{buildroot}%{_bindir}'
  mv "%{buildroot}%{python3_sitearch}/share/man/man1/${cmd}.1" \
      '%{buildroot}%{_mandir}/man1'
  # Replace the copies of the binaries inside the Python package with symbolic
  # links to %%{_bindir}, and make them relative so that they work both inside
  # the buildroot and in the installed package.
  ln -svf "%{buildroot}%{_bindir}/${cmd}" \
      "%{buildroot}%{python3_sitearch}/dcm2niix/${cmd}"
  symlinks -c "%{buildroot}%{python3_sitearch}/dcm2niix/${cmd}"
done
rm -rv "%{buildroot}%{python3_sitearch}/bin" \
    "%{buildroot}%{python3_sitearch}/share"
# Now that we have replaced the binaries with symlinks, the Python package is
# arch-independent.
if [ '%{python3_sitelib}' != '%{python3_sitearch}' ]
then
  install -d '%{buildroot}%{python3_sitelib}'
  mv %{buildroot}%{python3_sitearch}/dcm2niix* '%{buildroot}%{python3_sitelib}'
  sed -r -i 's@%{python3_sitearch}@%{python3_sitelib}@' %{pyproject_files}
fi


%check
%pyproject_check_import


%files
%doc README.md VERSIONS.md
%license license.txt
%if %{with jpegls} || %{with jnifti}
%license license-*.txt
%endif
%{_bindir}/dcm2niix
%{_bindir}/dcm2niibatch
%{_mandir}/man1/dcm2niix.1*
%{_mandir}/man1/dcm2niibatch.1*


%files -n python3-dcm2niix -f %{pyproject_files}


%changelog
%autochangelog
