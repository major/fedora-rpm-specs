%global commit da35f9d6c7374a95353fd1df1d394d44ab66cf01
%global snapdate 20240226

Name:           dr_libs
# While the individual header-only libraries are versioned, the overall
# collection is not, and there are no releases. These libraries follow the
# general practices of stb, so see also:
#   https://github.com/nothings/stb/issues/359
#   https://github.com/nothings/stb/issues/1101
%global snapinfo ^%{snapdate}git%{sub %{commit} 1 7}
Version:        0%{snapinfo}
Release:        %autorelease
Summary:        Single-file audio decoding libraries for C/C++

URL:            https://github.com/mackron/dr_libs
# See LICENSE.
License:        Unlicense OR MIT-0
# Additionally, the following are under different terms, but are not used; to
# make certain, they are removed in %%prep.
#
# - old/*.h are Unlicense (only)

%global dr_flac_version 0.12.42
%global dr_mp3_version 0.6.39
%global dr_wav_version 0.13.16

Source0:        %{url}/archive/%{commit}/dr_libs-%{commit}.tar.gz
# Upstream does not provide a build system for the tests. We have written a
# downstream Makefile that builds and runs all but the “playback” tests. (We do
# not want to handle those, since they requires sound hardware on the build
# host, and also require an additional “minaudio” dependency.)
Source1:        Makefile

# Upstream instructs that the FLAC library should be tested with the FLAC files
# from https://media.xiph.org/. Normally, we would like to test the code the
# same way upstream recommends, but there are some reasons not to:
#
#   • There is not a single-file archive for these, so we would have a number
#     of individual sources. This is annoying but workable.
#   • These files are HUGE—over 2GiB in total—yet not particularly designed to
#     exercise a large variety of decoder feeatures. The limited benefit of
#     packaging them all in the source RPM does not seem worth the cost in
#     storage and bandwidth.
#
# We compromise by picking only the single smallest FLAC to test. The Source#:
# declarations for the remaining FLAC files and archives of FLAC files are
# preserved as comments below.
#
# Note that none of the FLAC files used for testing are installed, so their
# licenses do not affect the License field.

# From short film “Elephant’s Dream”, CC-BY:
#   https://media.xiph.org/ED/readme.txt
#   https://media.xiph.org/ED/ED-CM-readme.txt
# Having the README in the SRPM ensures we satisfy CC-BY.
#Source100:      https://media.xiph.org/ED/EC-CM-readme.txt
#Source101:      https://media.xiph.org/ED/ED-CM-5.1-DVD-C.flac
#Source102:      https://media.xiph.org/ED/ED-CM-5.1-DVD-L.flac
#Source103:      https://media.xiph.org/ED/ED-CM-5.1-DVD-LFE.flac
#Source104:      https://media.xiph.org/ED/ED-CM-5.1-DVD-LS.flac
#Source105:      https://media.xiph.org/ED/ED-CM-5.1-DVD-R.flac
#Source106:      https://media.xiph.org/ED/ED-CM-5.1-DVD-RS.flac
#Source107:      https://media.xiph.org/ED/ED-CM-5.1-DVD.flac
#Source108:      https://media.xiph.org/ED/ED-CM-St-16bit.flac

# From short film “Big Buck Bunny”, CC-BY:
#   https://peach.blender.org/about/
#   https://media.xiph.org/BBB/bbb3d/README.txt
# Having the README in the SRPM ensures we satisfy CC-BY.
#Source110:      https://media.xiph.org/BBB/bbb3d/README.txt#/BBB-README.txt
#Source111:      https://media.xiph.org/BBB/BigBuckBunny-DVDMaster-5_1-FLAC.zip
#Source112:      https://media.xiph.org/BBB/BigBuckBunny-stereo.flac
#Source113:      https://media.xiph.org/BBB/BigBuckBunny-surround.flac
#Source114:      https://media.xiph.org/BBB/bbb3d/audio/bbb3d_sunflower_soundtrack_surround.flac

# From short film “Sintel”, CC-BY:
#   https://durian.blender.org/about/
#   https://media.xiph.org/sintel/README.txt
# Having the README in the SRPM ensures we satisfy CC-BY.
Source120:      https://media.xiph.org/sintel/README.txt#/sintel-README.txt
#Source121:      https://media.xiph.org/sintel/Jan_Morgenstern-Sintel-FLAC.zip
#Source122:      https://media.xiph.org/sintel/sintel-master-51-flac.zip
#Source123:      https://media.xiph.org/sintel/sintel-master-51.flac
#Source124:      https://media.xiph.org/sintel/sintel-master-st.flac
Source125:      https://media.xiph.org/sintel/sintel_trailer-audio.flac

# From short film “Tears of Steel”, CC-BY:
#   https://media.xiph.org/tearsofsteel/README.txt
# Having the README in the SRPM ensures we satisfy CC-BY.
#Source130:      https://media.xiph.org/tearsofsteel/README.txt#/tearsofsteel-README.txt
#Source131:      https://media.xiph.org/tearsofsteel/tearsofsteel-stereo.flac
#Source132:      https://media.xiph.org/tearsofsteel/tearsofsteel-surround.flac

# From short film “Cosmos Laundromat”, CC-BY-SA:
#   https://media.xiph.org/cosmoslaundromat/README.txt
# Having the README in the SRPM ensures we satisfy CC-BY-SA.
#Source140:      https://media.xiph.org/cosmoslaundromat/README.txt#/cosmoslaundromat-README.txt
#Source141:      https://media.xiph.org/cosmoslaundromat/Cosmos_Laundromat_1.flac

# For tests:
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(sndfile)

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%description
%{summary}.


%package devel
Summary:        Development files for dr_libs

BuildArch:      noarch

# Dependent packages should prefer to BuildRequire the -static packages for the
# specific dr_libs libraries they use.
Provides:       dr_libs-static = %{version}-%{release}

Requires:       dr_flac-devel = %{dr_flac_version}%{snapinfo}-%{release}
Requires:       dr_flac-static = %{dr_flac_version}%{snapinfo}-%{release}
Requires:       dr_mp3-devel = %{dr_mp3_version}%{snapinfo}-%{release}
Requires:       dr_mp3-static = %{dr_mp3_version}%{snapinfo}-%{release}
Requires:       dr_wav-devel = %{dr_wav_version}%{snapinfo}-%{release}
Requires:       dr_wav-static = %{dr_wav_version}%{snapinfo}-%{release}

%description devel
The dr_libs-devel package contains libraries and header files for developing
applications that use dr_libs.

This is a metapackage that requires the -devel packages for all dr_libs
libraries.


%package -n dr_flac-devel
Summary:        FLAC audio decoder
Version:        %{dr_flac_version}%{snapinfo}

BuildArch:      noarch

Provides:       dr_flac-static = %{dr_flac_version}%{snapinfo}-%{release}

%description -n dr_flac-devel
FLAC audio decoder.


%package -n dr_mp3-devel
Summary:        MP3 audio decoder
Version:        %{dr_mp3_version}%{snapinfo}

BuildArch:      noarch

Provides:       dr_mp3-static = %{dr_mp3_version}%{snapinfo}-%{release}

%description -n dr_mp3-devel
MP3 audio decoder. Based off minimp3 (https://github.com/lieff/minimp3).


%package -n dr_wav-devel
Summary:        WAV audio loader and writer
Version:        %{dr_wav_version}%{snapinfo}

BuildArch:      noarch

Provides:       dr_wav-static = %{dr_wav_version}%{snapinfo}-%{release}

%description -n dr_wav-devel
WAV audio loader and writer.


%package doc
Summary:        Documentation for dr_libs

BuildArch:      noarch

%description doc
Documentation for dr_libs.


%prep
%autosetup -n dr_libs-%{commit}

cp -p '%{SOURCE1}' tests/

# Remove some unused parts of the source tree that could contribute different
# (but acceptable) license terms if they were used—just to prove that we do not
# use them.
rm -rvf old

flacdir='tests/testvectors/flac/tests'
mkdir -p "${flacdir}"

cp -vp '%{SOURCE125}' "${flacdir}"
rm -rvf "${flacdir}/"*.md

# If we were testing with ALL of the FLAC files from from
# https://media.xiph.org/:

#cp -vp \
#    '%%{SOURCE101}' '%%{SOURCE102}' '%%{SOURCE103}' '%%{SOURCE104}' \
#      '%%{SOURCE105}' '%%{SOURCE106}' '%%{SOURCE107}' '%%{SOURCE108}' \
#    '%%{SOURCE112}' '%%{SOURCE113}' '%%{SOURCE114}' \
#    '%%{SOURCE123}' '%%{SOURCE124}' '%%{SOURCE125}' \
#    '%%{SOURCE131}' '%%{SOURCE132}' \
#    '%%{SOURCE141}' \
#    "${flacdir}"
#for zipfile in '%%{SOURCE111}' '%%{SOURCE121}' '%%{SOURCE122}'
#do
#  unzip "${zipfile}" -d "${flacdir}"
#done
#mv -v \
#    "${flacdir}/Jan_Morgenstern-Sintel-FLAC/"*.flac \
#    "${flacdir}/sintel-master-51-flac/"*.flac \
#    "${flacdir}"
#rm -rvf \
#    "${flacdir}/Jan_Morgenstern-Sintel-FLAC" \
#    "${flacdir}/sintel-master-51-flac" \
#    "${flacdir}/__MACOSX" \
#    "${flacdir}/"*.md


%build
# There is no compiled code to install, since all dr_libs libraries are
# header-only. We do need to build the tests.
%make_build -C tests


%install
install -t '%{buildroot}%{_includedir}' -p -m 0644 -D dr_*.h


%check
# We could append -j1 to override _smp_mflags and prevent interleaving of test
# output lines—at the cost of slower execution, of course.
%make_build -C tests check

# As a sanity check, verify that all of the subpackage version numbers appear
# in the corresponding headers.
while read -r version header
do
  grep -E "\\bv$(echo "${version}" | sed -r 's/\./\\./g')\\b" \
      "%{buildroot}%{_includedir}/${header}" >/dev/null
done <<'EOF'
%{dr_flac_version} dr_flac.h
%{dr_mp3_version} dr_mp3.h
%{dr_wav_version} dr_wav.h
EOF


%files devel
# Empty metapackage


%files doc
%license LICENSE
%doc README.md


%files -n dr_flac-devel
%license LICENSE
%{_includedir}/dr_flac.h


%files -n dr_mp3-devel
%license LICENSE
%{_includedir}/dr_mp3.h


%files -n dr_wav-devel
%license LICENSE
%{_includedir}/dr_wav.h


%changelog
%autochangelog
