%global forgeurl https://github.com/Guts/mkdocs-rss-plugin

Name:           python-mkdocs-rss-plugin
Version:        1.17.1
Release:        %autorelease
Summary:        MkDocs plugin which generates a static RSS feed

License:        MIT
URL:            https://guts.github.io/mkdocs-rss-plugin/
# PyPI tarball is missing requirements
Source:         %{forgeurl}/archive/%{version}/mkdocs-rss-plugin-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sed

%global _description %{expand:
This package provides a plugin for MkDocs, the static site generator, which
creates RSS 2.0 and JSON Feed 1.1 feeds using the creation and modification
dates from git log and page metadata (YAML frontmatter).}

%description %_description

%package -n     python3-mkdocs-rss-plugin
Summary:        %{summary}

%description -n python3-mkdocs-rss-plugin %_description

%prep
%autosetup -p1 -n mkdocs-rss-plugin-%{version}

# Relax version pins for test dependencies
sed -i 's/>=.*$//g' requirements/testing.txt

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkdocs_rss_plugin

%check
# Some tests assume to be inside a git repo
mkdir -p .git
# Disable tests that require Internet access
%pytest -v \
  --deselect=tests/test_build.py::TestBuildRss::test_date \
  --deselect=tests/test_build.py::TestBuildRss::test_json_feed_validation \
  --deselect=tests/test_build.py::TestBuildRss::test_not_in_git_log \
  --deselect=tests/test_build.py::TestBuildRss::test_rss_feed_validation \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_complete \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_custom_output_basename \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_custom_title_description \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_feed_length \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_feed_ttl \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_item_categories_enabled \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_item_comments_disabled \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_item_comments_enabled \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_item_dates \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_item_delimiter \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_item_delimiter_empty \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_item_length_unlimited \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_jsonfeed_enabled_not_rss \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_language_specific_material \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_locale_with_territory \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_locale_without_territory \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_minimal \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_multiple_instances \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_override_per_page_rss_feed_description \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_pretty_print_disabled \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_pretty_print_enabled \
  --deselect=tests/test_build.py::TestBuildRss::test_simple_build_rss_enabled_not_jsonfeed \
  --deselect=tests/test_integrations_material_social_cards.py::TestRssPluginIntegrationsMaterialSocialCards::test_simple_build \
  --deselect=tests/test_rss_util.py::TestRssUtil::test_remote_image_ok \
  %{nil}

%files -n python3-mkdocs-rss-plugin -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog
