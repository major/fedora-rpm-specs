Name:           python-mkdocs-include-markdown-plugin
Version:        7.1.2
Release:        %autorelease
Summary:        Mkdocs Markdown includer plugin

License:        Apache-2.0
URL:            https://github.com/mondeja/mkdocs-include-markdown-plugin
# PyPI tarball doesn't include tests
Source:         %{url}/archive/v%{version}/mkdocs-include-markdown-plugin-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This package provides an Mkdocs Markdown includer plugin.}

%description %_description

%package -n     python3-mkdocs-include-markdown-plugin
Summary:        %{summary}

%description -n python3-mkdocs-include-markdown-plugin %_description

%pyproject_extras_subpkg -n python3-mkdocs-include-markdown-plugin cache

%prep
%autosetup -p1 -n mkdocs-include-markdown-plugin-%{version}

%generate_buildrequires
%pyproject_buildrequires -x cache

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkdocs_include_markdown_plugin

%check
# Disable tests that require Internet access
%pytest -v \
  --deselect='tests/test_integration/test_cache_integration.py::test_page_included_by_url_is_cached[directive=include-https://raw.githubusercontent.com/mondeja/mkdocs-include-markdown-plugin/master/examples/basic/mkdocs.yml-site_name: Foo\nplugins:\n ' \
  --deselect='tests/test_integration/test_cache_integration.py::test_page_included_by_url_is_cached[directive=include-https://raw.githubusercontent.com/mondeja/mkdocs-include-markdown-plugin/master/examples/basic/docs/included.md-Some ignored content.\n\n<--start-->\n\nSome included content.\n]' \
  --deselect='tests/test_integration/test_cache_integration.py::test_page_included_by_url_is_cached[directive=include-markdown-https://raw.githubusercontent.com/mondeja/mkdocs-include-markdown-plugin/master/examples/basic/mkdocs.yml-site_name: Foo\nplugins:\n ' \
  --deselect='tests/test_integration/test_cache_integration.py::test_page_included_by_url_is_cached[directive=include-markdown-https://raw.githubusercontent.com/mondeja/mkdocs-include-markdown-plugin/master/examples/basic/docs/included.md-Some ignored content.\n\n<--start-->\n\nSome included content.\n]' \
  --deselect='tests/test_integration/test_examples.py::test_examples_subprocess[http-cache-dir]' \
  --deselect='tests/test_integration/test_examples.py::test_examples_subprocess[http-cache]' \
  --deselect='tests/test_integration/test_examples.py::test_examples_api[http-cache-dir]' \
  --deselect='tests/test_integration/test_examples.py::test_examples_api[http-cache]' \
  --deselect='tests/test_unit/test_include.py::test_include[url]' \
  --deselect='tests/test_unit/test_include_markdown.py::test_include_markdown[url]' \
  --deselect='tests/test_unit/test_process.py::test_read_url_cached_content' \
  %{nil}

%files -n python3-mkdocs-include-markdown-plugin -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
