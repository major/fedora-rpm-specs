Name:           python-zhon
Version:        2.1.1
Release:        %autorelease
Summary:        Zhon provides constants used in Chinese text processing


License:        MIT
URL:            https://github.com/tsroten/zhon
Source:         %{url}/archive/v%{version}/zhon-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)

%global _description %{expand:
Zhon is a Python library that provides constants commonly used in Chinese text
processing.  Zhon includes the following commonly-used constants:
- CJK characters and radicals
- Chinese punctuation marks
- Chinese sentence regular expression pattern
- Pinyin vowels, consonants, lowercase, uppercase, and punctuation
- Pinyin syllable, word, and sentence regular expression patterns
- Zhuyin characters and marks
- Zhuyin syllable regular expression pattern
- CC-CEDICT characters}

%description %_description

%package -n     python3-zhon
Summary:        %{summary}

%description -n python3-zhon %_description


%prep
%autosetup -n zhon-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
# build documentation
pushd docs
sphinx-build -b text .  text
popd

%install
%pyproject_install
%pyproject_save_files zhon


%check
%pyproject_check_import
%pytest

%files -n python3-zhon -f %{pyproject_files}
%doc docs/text/api.txt
%doc docs/text/authors.txt
%doc docs/text/contributing.txt
%doc docs/text/history.txt

%changelog
%autochangelog
