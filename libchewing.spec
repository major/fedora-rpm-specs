%global libchewing_python_dir %{python3_sitelib}

%global im_name_zh_TW 新酷音輸入法
%global name_zh_TW %{im_name_zh_TW}函式庫

Name:           libchewing
Version:        0.6.0
Release:        %autorelease
Summary:        Intelligent phonetic input method library for Traditional Chinese
Summary(zh_TW): %{name_zh_TW}

License:        LGPLv2+
URL:            https://chewing.im
Source0:        https://github.com/chewing/%{name}/releases/download/v%{version}/libchewing-%{version}.tar.xz

BuildRequires:  gcc g++ cmake pkgconfig texinfo
BuildRequires:  sqlite-devel
BuildRequires:  python3-devel
BuildRequires: make
Requires: sqlite
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
%setup -q

%build
%cmake --preset default
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{libchewing_python_dir}
cp -p contrib/python/chewing.py %{buildroot}%{libchewing_python_dir}

rm -f %{buildroot}/%{_infodir}/dir

%check
%ctest -j1

%files
%doc README.md AUTHORS COPYING NEWS
%{_datadir}/%{name}/
%{_libdir}/*.so.*
%{_infodir}/%{name}.info.*

%files devel
%dir %{_includedir}/chewing
%{_includedir}/chewing/*
%{_libdir}/pkgconfig/chewing.pc
%{_libdir}/*.so

%files -n python3-%{name}
%{libchewing_python_dir}/chewing.py
%{libchewing_python_dir}/__pycache__/*

%changelog
%autochangelog
