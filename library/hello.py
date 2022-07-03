from ansible.module_utils.basic import AnsibleModule


def run_module():
    mod_args = {
        "name": {"type": str, "required": True}
    }

    module = AnsibleModule(argument_spec=mod_args, supports_check_mode=False)

    module.exit_json(
        changed=False,
        message=f"Hello, {module.params['name']}!"
    )


if __name__ == '__main__':
    run_module()
