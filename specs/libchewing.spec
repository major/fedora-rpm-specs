%bcond_without check
%global libchewing_python_dir %{python3_sitelib}

%global im_name_zh_TW 新酷音輸入法
%global name_zh_TW %{im_name_zh_TW}函式庫

Name:           libchewing
Version:        0.10.2
Release:        %autorelease
Summary:        Intelligent phonetic input method library for Traditional Chinese
Summary(zh_TW): %{name_zh_TW}

# Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# LGPL-2.1-or-later
# MIT
# MIT OR Apache-2.0
# MPL-2.0
License:        LGPL-2.1-or-later AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND MPL-2.0
# LICENSE.dependencies contains a full license breakdown

URL:            https://chewing.im
Source0:        https://github.com/chewing/%{name}/releases/download/v%{version_no_tilde}/libchewing-%{version_no_tilde}.tar.zst
Source1:        https://github.com/chewing/%{name}/releases/download/v%{version_no_tilde}/libchewing-%{version_no_tilde}.tar.zst.asc
Source2:        https://chewing.im/.well-known/openpgpkey/hu/y84sdmnksfqswe7fxf5mzjg53tbdz8f5?l=release#/libchewing.pgp

Patch:          0001-Delete-unused-optional-dependencies.patch

BuildRequires:  gcc cmake make pkgconf texinfo
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  cmake(Corrosion)
BuildRequires:  gnupg2
BuildRequires:  python3-devel
# since f31
Obsoletes:      python2-libchewing < 0.5.1-13

%description
libchewing is an intelligent phonetic input method library for Chinese.

It provides the core algorithm and logic that can be used by various
input methods. The Chewing input method is a smart bopomofo phonetics
input method that is useful for inputting Mandarin Chinese.

%description -l zh_TW
%{name_zh_TW}提供實做了核心選字演算法，以便輸入法程式調用。

%{im_name_zh_TW}是一種智慧型注音/拼音猜字輸入法，透過智慧型的字庫分析、習慣記錄學習與預測分析，
使拼字輸入的人為選字機率降至最低，進而提升中文輸入、打字的效率。

%package -n %{name}-devel
Summary:        Development files for libchewing
Summary(zh_TW): %{name_zh_TW}開發者套件
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}-devel
Headers and other files needed to develop applications using the %{name}
library.

%description -l zh_TW  -n %{name}-devel
%{name_zh_TW}開發者套件提供了開發%{im_name_zh_TW}相關程式所需的檔案，
像是標頭檔(header files)，以及函式庫。


%package -n python3-%{name}
Summary:        Python binding for libchewing
BuildArch:      noarch
Summary(zh_TW): %{name_zh_TW} python 綁定
Requires:       %{name} = %{version}-%{release}

%description -n python3-%{name}
Python binding of libchewing.

%description -l zh_TW -n python3-%{name}
%{name_zh_TW} python 綁定

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n libchewing-%{version_no_tilde}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cmake --preset default
%cmake_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cmake_install

mkdir -p %{buildroot}%{libchewing_python_dir}
cp -p contrib/python/chewing.py %{buildroot}%{libchewing_python_dir}

rm -f %{buildroot}/%{_infodir}/dir

%if %{with check}
%check
%ctest -j1
%endif

%files
%license COPYING
%license LICENSE.dependencies
%doc README.md AUTHORS NEWS
%{_datadir}/%{name}/
%{_bindir}/chewing-cli
%{_libdir}/libchewing.so.*
%{_infodir}/%{name}.info.*
%{_mandir}/man1/chewing-cli*

%files devel
%dir %{_includedir}/chewing
%{_includedir}/chewing/*
%{_libdir}/pkgconfig/chewing.pc
%{_libdir}/libchewing.so
%{_libdir}/cmake/Chewing/ChewingConfig.cmake
%{_libdir}/cmake/Chewing/ChewingConfigVersion.cmake
%{_libdir}/cmake/Chewing/ChewingTargets-release.cmake
%{_libdir}/cmake/Chewing/ChewingTargets.cmake


%files -n python3-%{name}
%{libchewing_python_dir}/chewing.py
%{libchewing_python_dir}/__pycache__/*

%changelog
%autochangelog
