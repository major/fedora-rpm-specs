%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

%global server_dir %{_libexecdir}/fcitx5-mozc

Name:           fcitx5-mozc
%global forgeurl https://github.com/fcitx/mozc
%global commit 0cd24273e73ab360c8dbb6e2a94acb135743ee13
%global archivename %{name}-%{commit}
%forgemeta 

Version:        2.17.2102.102.1
# upstream don't tag release, build git snapshot here
# git snaoshot should have s snapshot date will be taken care
# of by forgemeta after importing to dist-git
Release:        %autorelease
Summary:        A wrapper of mozc for fcitx5
# fcitx5-mozc is a fork of mozc, difference can be seen at 
# https://github.com/google/mozc/compare/master...fcitx:fcitx
# src/third_party/abseil-cpp : Apache License
# src/third_party/breakpad : BSD License
# src/third_party/japanese_usage_dictionary: BSD license
# src/third_party/wtl: MS-PL
# src/unix/fcitx5: LGPLv2+
# ----
# data/unicode/: UCD
#  Copyright (c) 1991-2008 Unicode, Inc.
# data/test/stress_test/sentences.txt: Public Domain
# data/dictionary_oss/: mecab-ipadic and BSD
#   See http://code.google.com/p/mozc/issues/detail?id=20
#   also data/installer/credits_en.html
# src/data/test/dictionary/: same as data/dictionary_oss
License:        BSD and ASL 2.0 and UCD and Public Domain and mecab-ipadic and LGPLv2+ and MS-PL
URL:            %{forgeurl}

# The source of this package was pulled from upstreams's vcs.
# Use the following command to generate the tar ball:
# with gtest gyp jsoncpp protobuf unbundled 
# abseil-cpp is left here due to hardcoded build scripts from
# upstream code.
# -----
# git clone --recursive https://github.com/fcitx/mozc.git --depth 1
# cd mozc
# git checkout %%{commit}
# for i in gtest gyp jsoncpp protobuf ; do rm -rf src/third_party/$i; done
# cd ..
# tar --exclude-vcs -czf %%{name}-%%{commit}.tar.gz mozc/
# -----
Source0:        %{name}-%{commit}.tar.gz
# Public Domain
Source1:        http://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip
Source2:        http://www.post.japanpost.jp/zipcode/dl/jigyosyo/zip/jigyosyo.zip

# add -v to ninja command, to make verbose output during building
Patch0:         mozc-build-verbosely.patch

BuildRequires:  python3-devel
BuildRequires:  gettext 
BuildRequires:  gtk2-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  zinnia-devel
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  gyp >= 0.1-0.4.840svn
BuildRequires:  fcitx5-devel
BuildRequires:  libappstream-glib
BuildRequires:  %{py3_dist six}
BuildRequires:  protobuf-devel 
BuildRequires:  protobuf-c
BuildRequires:  abseil-cpp-devel
BuildRequires:  gtest-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  binutils

Requires:       hicolor-icon-theme
Requires:       fcitx5
Requires:       fcitx5-data

# https://bugzilla.redhat.com/show_bug.cgi?id=1419949
# we are using mostly exact mozc server, same problem
# may occur here, adding ExcludeArch like ibus-mozc
ExcludeArch:    ppc ppc64 sparcv9 sparc64 s390x

%description
A wrapper of mozc for fcitx5.

%prep
%setup -q -n mozc -a 1 -a 2
%patch0 -p1
(cd src/data/dictionary_oss;
PYTHONPATH="${PYTHONPATH}:../../" python3 ../../dictionary/gen_zip_code_seed.py --zip_code=../../../KEN_ALL.CSV --jigyosyo=../../../JIGYOSYO.CSV >> dictionary09.txt;
)
# Don't build for fcitx4
rm src/unix/fcitx/fcitx.gyp
# building with gcc, change to add -lc++
sed "/stdlib=libc++/d;/-lc++/d" -i src/gyp/common.gypi
sed "s/clang++/c++/g" -i src/gyp/common.gypi
sed "s/clang/gcc/g" -i src/gyp/common.gypi
# preserve install time stamp
sed "s/ -m/ -pm/g" -i scripts/install_fcitx5 scripts/install_fcitx5_icons

%build
%set_build_flags
pushd src
# specify an another path for those mozc server files
# to enable this to co-exist with ibus-mozc
QTDIR=%{_prefix} \
GYP_DEFINES="document_dir=%{_datadir}/licenses/%{name} use_libzinnia=1 use_libprotobuf=1 zinnia_model_file=%{_datadir}/zinnia/model/tomoe/handwriting-ja.model" \
python3 build_mozc.py gyp --gypdir=%{_bindir} --server_dir=%{server_dir} --target_platform=Linux
python3 build_mozc.py build -c Release server/server.gyp:mozc_server gui/gui.gyp:mozc_tool unix/fcitx5/fcitx5.gyp:fcitx5-mozc
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
