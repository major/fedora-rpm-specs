%bcond bundle_abslcpp   0

# The latest version of fcitx5-mozc requires newer
# version of protobuf than we have in Fedora 
# Bundling it for now
%bcond bundle_protobuf  1

# Enabling test also requires gtest, and we have to
# bundle it since the build system is not designed to
# use system gtest, disabling it for now to avoid
# bundlings. 
%bcond run_test         0

%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

# as of 2025.1.1, build with gcc failed due to errors 
# with LOG(DFATAL), don't have time to investigate the 
# root cause. Switch to clang for now
%global toolchain clang

%global server_dir %{_libexecdir}/fcitx5-mozc


# main source 
%global forgeurl0 https://github.com/fcitx/mozc
%global commit0   c0ed34eaa1f39d2106554f4811969ebea04c1f0f

# BSD 2-Clause license
# src/third_party/japanese_usage_dictionary
%global forgeurl1 https://github.com/hiroyuki-komatsu/japanese-usage-dictionary
%global commit1   e5b3425575734c323e1d947009dd74709437b684

%if %{with bundle_protobuf}
# BSD 3-Clause
# src/third_party/protobuf
%global forgeurl2 https://github.com/protocolbuffers/protobuf
%global tag2      v3.29.1
%endif

%if %{with run_test}
# src/third_party/gtest
%global forgeurl3 https://github.com/google/googletest
%global tag3      v1.15.2
%endif

%if %{with bundle_abslcpp}
%global forgeurl4 https://github.com/abseil/abseil-cpp
%global tag4      20240722.0
%endif

%forgemeta -a

Name:           fcitx5-mozc
# keep version consistent with mozc version 
# that fcitx5-mozc is based on
Version:        2.30.5618.102
# upstream don't tag release, build git snapshot here
# git snapshot should have snapshot date will be taken care
# of by forgemeta after importing to dist-git
Release:        %autorelease
Summary:        A wrapper of mozc for fcitx5
License:        BSD and UCD and Public Domain and mecab-ipadic and LGPLv2+ and MS-PL
URL:            %{forgeurl}

# main source
Source0:        %{forgesource0} 
Source1:        %{forgesource1} 

%if %{with bundle_protobuf}
# protobuf
Source2:        %{forgesource2} 
%endif

%if %{with run_test}
# gtest
Source3:        %{forgesource3} 
%endif

%if %{with bundle_abslcpp}
# abseil-cpp
Source4:        %{forgesource4}
%endif

# Public Domain
Source5:        http://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip
Source6:        http://www.post.japanpost.jp/zipcode/dl/jigyosyo/zip/jigyosyo.zip

# add -v to ninja command, to make verbose output during building
Patch0:         mozc-build-verbosely.patch
%if %{without bundle_abslcpp}
Patch1:         0001-use-system-absl.patch
%endif

BuildRequires:  python3-devel
BuildRequires:  gettext 
BuildRequires:  gtk2-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  zinnia-devel
BuildRequires:  clang
BuildRequires:  ninja-build
BuildRequires:  gyp >= 0.1-0.4.840svn
BuildRequires:  fcitx5-devel
BuildRequires:  libappstream-glib
BuildRequires:  %{py3_dist six}
# BuildRequires:  gtest-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  binutils

Requires:       hicolor-icon-theme
Requires:       fcitx5
Requires:       fcitx5-data

%if %{with bundle_protobuf}
Provides:       bundled(protobuf) = %{tag2}
%else
BuildRequires:  protobuf-devel 
BuildRequires:  protobuf-c
%endif

%if %{with bundle_abslcpp}
Provides:       bundled(abseil-cpp) = %{tag4}
%else
BuildRequires:  abseil-cpp-devel
%endif

# https://bugzilla.redhat.com/show_bug.cgi?id=1419949
# we are using mostly exact mozc server, same problem
# may occur here, adding ExcludeArch like ibus-mozc
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    ppc ppc64 sparcv9 sparc64 s390x %{ix86}

%description
A wrapper of mozc for fcitx5.

%prep
%setup -q -n %{archivename0} -a 5 -a 6
rm -rf src/third_party/*

%setup -q -n %{archivename0} -T -D -a 1
mv %{archivename1} src/third_party/japanese_usage_dictionary

%if %{with bundle_protobuf}
%setup -q -n %{archivename0} -T -D -a 2
mv %{archivename2} src/third_party/protobuf
rm src/third_party/protobuf/src/google/protobuf/lazy_repeated_field.cc
rm src/third_party/protobuf/src/google/protobuf/lazy_repeated_field_heavy.cc
%endif

%if %{with run_test}
%setup -q -n %{archivename0} -T -D -a 3
mv %{archivename3} src/third_party/gtest
%endif

%if %{with bundle_abslcpp}
%setup -q -n %{archivename0} -T -D -a 4
mv %{archivename4} src/third_party/abseil-cpp
%endif



%patch 0 -p1

%if %{without bundle_abslcpp}
%patch 1 -p1
%endif

(cd src/data/dictionary_oss;
PYTHONPATH="${PYTHONPATH}:../../" python3 ../../dictionary/gen_zip_code_seed.py \
    --zip_code=../../../KEN_ALL.CSV --jigyosyo=../../../JIGYOSYO.CSV >> dictionary09.txt;
)
# Don't build for fcitx4
rm src/unix/fcitx/fcitx.gyp
# preserve install time stamp
sed "s/ -m/ -pm/g" -i scripts/install_fcitx5 scripts/install_fcitx5_icons

%build
%set_build_flags
pushd src
# specify an another path for those mozc server files
# to enable this to co-exist with ibus-mozc
QTDIR=%{_prefix} \
GYP_DEFINES="document_dir=%{_datadir}/licenses/%{name} \
    use_libzinnia=1 %{!?with_bundle_abslcpp:use_system_abseil_cpp=1} \
    %{?with_bundle_protobuf:use_libprotobuf=0} %{!?with_bundle_protobuf:use_libprotobuf=1} \
    zinnia_model_file=%{_datadir}/zinnia/model/tomoe/handwriting-ja.model" \
python3 build_mozc.py gyp --gypdir=%{_bindir} --server_dir=%{server_dir} --target_platform=Linux

# some race condition that the build system can fail due to genproto_commands_proto
# not finished before its dependents, so build it separately
python3 build_mozc.py build -c Release  protocol/protocol.gyp:genproto_commands_proto
python3 build_mozc.py build -c Release  server/server.gyp:mozc_server \
                                        gui/gui.gyp:mozc_tool \
                                        unix/fcitx5/fcitx5.gyp:fcitx5-mozc
popd

%install
pushd src
export _bldtype=Release
install -D -pm 755 "out_linux/${_bldtype}/mozc_server" "%{buildroot}%{server_dir}/mozc_server"
install -D -pm 755 "out_linux/${_bldtype}/mozc_tool"   "%{buildroot}%{server_dir}/mozc_tool"
# fix install dirs in script, don't use those hardcoded paths: 
# ${PREFIX}/share/metainfo -> _metainfodir
sed "s|\${PREFIX}/share/metainfo|%{buildroot}%{_metainfodir}|g" -i  ../scripts/install_fcitx5 ../scripts/install_fcitx5_data
# ${PREFIX}/share -> _datadir
sed "s|\${PREFIX}/share|%{buildroot}%{_datadir}|g"              -i  ../scripts/install_fcitx5 ../scripts/install_fcitx5_icons ../scripts/install_fcitx5_data
# ${PREFIX}/lib -> _libdir
sed "s|\${PREFIX}/lib|%{buildroot}%{_libdir}|g"                 -i  ../scripts/install_fcitx5
../scripts/install_fcitx5 
popd

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%find_lang %{name}

%if %{with run_test}
%check
pushd src
python3 build_mozc.py runtests -c Release
%endif

%files -f %{name}.lang
%license LICENSE 
%doc README.md src/data/installer/*.html
%{server_dir}
%{_datadir}/fcitx5/*/mozc.conf
%{_datadir}/icons/hicolor/*/apps/*
%{_libdir}/fcitx5/fcitx5-mozc.so
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Mozc.metainfo.xml

%changelog
%autochangelog
