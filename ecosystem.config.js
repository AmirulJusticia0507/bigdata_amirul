module.exports = {
    apps: [
      {
        name: "bigdata_amirul",
        script: "manage.py",
        args: ["runserver", "127.0.0.1:8000"],
        exec_mode: "fork",
        instances: "1",
        watch: true,
        wait_ready: true,
        autorestart: false,
        max_restart: 5,
        exec_interpreter: "python",
        env: {
          DJANGO_SETTINGS_MODULE: "core.settings",
        },
      },
    ],
  };
  